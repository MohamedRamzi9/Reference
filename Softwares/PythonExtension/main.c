#define PY_SSIZE_T_CLEAN // This must be defined before including Python.h to use Py_ssize_t
#include <Python.h> // Include the Python C API header to access Python's C functions and types


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

PyMethodDef ModuleMethods[] = { // Python method definitions, an array of PyMethodDef structures that define the methods of the module
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
    {NULL, NULL, 0, NULL} // last entry must be a sentinel with NULL values to indicate the end of the array
};

struct PyModuleDef moduledef = { // Module definition structure, defines the properties of the module
    PyModuleDef_HEAD_INIT, // Macro to initialize the module definition structure
    "module", // name of the module, this is the name that will be used to import the module in Python
    NULL, // module documentation string, can be NULL if no documentation is provided
    -1, // size of the module state, -1 means the module keeps state in global variables, otherwise it should be the size of the module state structure
    ModuleMethods // pointer to the array of method definitions, this tells Python which functions are available in the module
};

PyMODINIT_FUNC PyInit_module(void) { // Module initialization function, declared with PyMODINIT_FUNC to ensure the correct calling convention is used, the name must be "PyInit_" followed by the module name, is called when the module is imported in Python
    return PyModule_Create(&moduledef); // must return a new reference to the module object using PyModule_Create, which takes a pointer to the module definition structure and creates the module object based on it
}
