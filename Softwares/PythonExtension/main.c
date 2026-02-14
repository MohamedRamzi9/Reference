#define PY_SSIZE_T_CLEAN // This must be defined before including Python.h to use Py_ssize_t
#include <Python.h> // Include the Python C API header to access Python's C functions and types

PyObject* hello(PyObject* self, PyObject* args) { // Define a C function that will be exposed to Python, returns PyObject*, always takes two arguments: PyObject* argument for the module (self) and PyObject* for the list of arguments passed from Python (args) which can be empty
    printf("Hello, World!\n"); // C code 
    Py_RETURN_NONE; // Macro to return None in Python, equivalent to "return Py_None;" but also increments the reference count of Py_None
}

PyMethodDef ModuleMethods[] = { // Python method definitions, an array of PyMethodDef structures that define the methods of the module
    {
        "hello", // name of the method that will be used in Python to import and call the function
        hello, // pointer to the C function that implements the method
        METH_NOARGS, // flag that indicates how the function should be called, METH_NOARGS: takes no arguments, METH_VARARGS: takes a tuple of arguments, METH_KEYWORDS: takes a tuple of arguments and a dictionary of keyword arguments
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
