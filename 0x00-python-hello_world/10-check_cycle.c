#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle or not
 * @list: a linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list, *ptr2 = list;
	int n = 1, m;
	while (ptr != NULL)
	{
		m = n;
		while (m != 0)
		{
			if (ptr->next == ptr2)
				return (1);
			ptr2 = ptr2->next;
			m--;
		}
		ptr = ptr->next;
		ptr2 = list;
		n++;
	}
	return (0);
}
