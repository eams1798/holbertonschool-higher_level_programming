#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle or not
 * @list: a linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list;
	while (ptr->next != NULL)
	{
		if (ptr->next == list)
			return (1);
		ptr = ptr->next;
	}
	return (0);
}
