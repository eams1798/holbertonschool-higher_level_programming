#include <Python.h>

void print_python_list_info(PyObject *p)
{
	PyObject* obj;
	PyListObject *plist = (PyListObject *)p;
	PyTypeObject* type;
	const char *strtype;
	int len = (int)PyList_Size(p), i, pylloc;

	pylloc = (int)plist->allocated;
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", pylloc);
	for (i = 0; i < len; i++)
	{
		obj = PyList_GetItem(p, i);
		type = Py_TYPE(obj);
		strtype = type->tp_name;
		printf("Element %d: %s\n", i, strtype);
	}
}
