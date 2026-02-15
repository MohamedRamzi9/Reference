#define PY_SSIZE_T_CLEAN // This must be defined before including Python.h to use Py_ssize_t
#include "Python.h" // Include the Python C API header to access Python's C functions and types
#include "structmember.h" // Include the header for defining members of Python class types

PyObject* method_with_varargs(PyObject* self, PyObject* args) { // Define a C function that returns PyObject* and takes 2 arguments: PyObject* self refering to the module and PyObject* args which can be one of : tuple of arguments (with METH_VARARGS), one argument (with METH_O) or NULL (with METH_NOARGS)
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) { // Parse the arguments from the args tuple using PyArg_ParseTuple which returns 1 on success and 0 on failure, the format for each argument is : i: int, s: string (char*), f: float (double), O: object (PyObject*)
        return NULL; // If parsing fails, return NULL to indicate an error
    }
    printf("The sum of %d and %d is %d\n", a, b, a + b);
    Py_RETURN_NONE; // Macro to return None in Python, equivalent to "return Py_None;" but also increments the reference count of Py_None
}

PyObject* method_with_varargs_and_keywords(PyObject* self, PyObject* args, PyObject* kwargs) { // same as method_with_varargs but also takes a PyObject* kwargs for keyword arguments (with METH_KEYWORDS), only keyword names are stored in the kwargs, the values are stored in args tuple, unless combined with METH_VARARGS, in which case the values are appended to the end of the args tuple after the positional arguments
    int a, b, c;
    static char* kwlist[] = {"b", "c", NULL}; // List of keyword argument names, must be NULL-terminated
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "i|ii", kwlist, &a, &b, &c)) { // Parse the arguments and keywords using PyArg_ParseTupleAndKeywords which returns 1 on success and 0 on failure, use | to separate positional arguments (if present) from optional arguments
        return NULL; // If parsing fails, return NULL to indicate an error
    }
    Py_RETURN_NONE;
}

PyMethodDef Methods[] = { // Python method definitions, an array of PyMethodDef structures that define the methods of the module or class depending on what it is attached to
    {
        "hello", // name of the method that will be used in Python to import and call the function
        method_with_varargs, // pointer to the C function that implements the method
        METH_VARARGS, // flag on how the function is called which can be one of the follwing :
            // METH_NOARGS: takes NULL for second argument
            // METH_VARARGS: takes a tuple of arguments
            // METH_O: takes a single object argument
            // METH_KEYWORDS: takes a tuple of arguments containing only keyword args and a dictionary of keyword names
            // METH_KEYWORDS | METH_VARARGS: takes a tuple of arguments containing both positional and keyword args and a dictionary of keyword names  
            // METH_STATIC: takes NULL for first argument (no self) and can be combined with any of the above flags to specify the other arguments
        "Print hello" // docstring for the method, can be NULL if no documentation is provided
    },
    {NULL} // last entry must be a sentinel with NULL values to indicate the end of the array
};



// ======================================
// ========== CLASS DEFINITION ==========
// ======================================

typedef struct { // underlying C structure for the Python class
    PyObject_HEAD // first member must be PyObject_HEAD which includes reference count and type information
    long value; // other members of the type can be defined after PyObject_HEAD 
} MyObject;



int MyObject_init(MyObject *self, PyObject *args, PyObject *kwds) { // init method for the class, must have this signature, where first argument is a pointer to the instance of the underlying C structure representing the type
    long value;

    if (!PyArg_ParseTuple(args, "l", &value))
        return -1;

    self->value = value; // access the members of the 
    return 0;
}

PyObject * MyObject_get_value(MyObject *self, PyObject* args) { // method for the class, must have this signature, where first argument is a pointer to the instance of the underlying C structure representing the type 
    return PyLong_FromLong(self->value);
}

static PyMethodDef MyObject_methods[] = { // methods table defition for the class, same as module method definitions
    {"get_value", MyObject_get_value, METH_NOARGS, "Return the stored value"},
    {NULL}
};

static PyMemberDef MyObject_members[] = { // members table definition for the class, an array of PyMemberDef structures that define the members of the class
    {
        .name = "value", // name of the member that will be used in Python to access the member 
        .type = T_LONG, // type of the member, can be one of the following : 
            // T_SHORT: short int
            // T_INT: int
            // T_LONG: long int
            // T_FLOAT: float
            // T_DOUBLE: double
            // T_STRING: char*
            // T_OBJECT_EX: PyObject* (with exception on NULL)
            // T_OBJECT: PyObject* (without exception on NULL)
        .offset = offsetof(MyObject, value), // offset of the member in the underlying C structure, preferably calculated using the offsetof macro to avoid errors not taking into account the size of the PyObject_HEAD
        .flags = 0, // flags for the member, can be one of the following :
            // READONLY: member is read-only and cannot be assigned to in Python
            // RO: same as READONLY
            // RESTRICTED: member is restricted and cannot be accessed directly in Python, but can be accessed through getter and setter methods defined in the tp_getset slot of the type object
            // 0: no flags, member can be read and assigned to in Python 
        .doc = "stored value" // docstring for the member, can be NULL if no documentation is provided
    },
    {NULL} // last entry must be a sentinel with NULL values to indicate the end of the array
};

PyTypeObject MyObjectType = { // type object definition for the class, an instance of PyTypeObject structure that defines the properties and behavior of the type, not all members must be initialized
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0) // Macro to initialize the type object structure, takes two arguments: pointer to the base type (NULL for new types) and size of the variable part of the object (0 for non-variable types)
    .tp_name = "module.MyObject", // name of the type in the format "ModuleName.TypeName", this is the name that will be used to import and create instances of the type in Python 
    .tp_basicsize = sizeof(MyObject), // size of the underlying C structure representing the type, used for memory allocation when creating instances of the type
    .tp_flags = Py_TPFLAGS_DEFAULT, // flags for the type, can be a combination of the following :
        // Py_TPFLAGS_DEFAULT: default flags for a new type, includes Py_TPFLAGS_HAVE_GC and Py_TPFLAGS_BASETYPE
        // Py_TPFLAGS_HAVE_GC: type supports garbage collection, necessary if the type has members that are Python objects to avoid memory leaks
        // Py_TPFLAGS_BASETYPE: type can be subclassed in Python, necessary if you want to allow users to create subclasses of your type in Python
    .tp_doc = "Simple example class", // docstring for the type, can be NULL if no documentation is provided
    .tp_methods = MyObject_methods, // pointer to the methods table for the type
    .tp_members = MyObject_members, // pointer to themembers table for the type
    .tp_init = MyObject_init, // pointer to the init function of the type
    .tp_new = PyType_GenericNew, // pointer to the new function of the type, use PyType_GenericNew for default behavior 
};


struct PyModuleDef moduledef = { // Module definition structure, defines the properties of the module
    PyModuleDef_HEAD_INIT, // Macro to initialize the module definition structure
    "module", // name of the module, this is the name that will be used to import the module in Python
    NULL, // module documentation string, can be NULL if no documentation is provided
    -1, // size of the module state, -1 means the module keeps state in global variables, otherwise it should be the size of the module state structure
    Methods // pointer to the array of method definitions, this tells Python which functions are available in the module
};

PyMODINIT_FUNC PyInit_module(void) { // Module initialization function, declared with PyMODINIT_FUNC to ensure the correct calling convention is used, the name must be "PyInit_" followed by the module name, is called when the module is imported in Python
    PyObject* m; // variable to hold the reference to the module object 

    if (PyType_Ready(&MyObjectType) < 0) // call PyType_Ready to initialize the type object, returns 0 on success and -1 on failure
        return NULL; // return NULL if initialization fails to indicate an error

    m = PyModule_Create(&moduledef); // create the module object using PyModule_Create and passing a pointer to the module definition structure
    if (m == NULL)
        return NULL;

    Py_INCREF(&MyObjectType); // increment the reference count of the type object using Py_INCREF Macro to compensate for the reference count decrement by PyModule_AddObject
    if (PyModule_AddObject(m, "MyObject", (PyObject *)&MyObjectType) < 0) { // add the type object to the module using PyModule_AddObject, takes three arguments: pointer to the module object, name of the attribute to add which must the same as the type name in the type object definition, and pointer to the type object casted to PyObject*, returns 0 on success and -1 on failure
        Py_DECREF(&MyObjectType); // decrement the reference count of the type object since adding it to the module failed so the reference count was not stolen by PyModule_AddObject
        Py_DECREF(m); // decrement the reference count of the module object since adding the type to the module failed so the module should be deallocated
        return NULL; // return NULL to indicate an error
    }

    return m; // return the module object
}
