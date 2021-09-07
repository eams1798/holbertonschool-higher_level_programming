#include "lists.h"

/**
 * define_node - create a defined node by the given number
 * @num: number for the node
 *
 * Return: the new node
 */
listint_t *define_node(int num)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = num;
	new->next = NULL;
	return (new);
}

/**
 * insert_node - insert a node into a sorted singly linked list
 * @head: the head of the linked list
 * @number: the number of the node to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *node = define_node(number);

	while (ptr != NULL)
	{
		if (ptr->next->n > node->n)
		{
			node->next = ptr->next;
			ptr->next = node;
			break;
		}
		ptr = ptr->next;
	}
	return (node);
}
