#include "lists.h"

/**
 * reverse - an auxiliar function to revert the linked list
 * @head: a list of elements with a pointer to the first element
 * @prev: a pointer to a node of the linked list
 * @node: a pointer to another node of the linked list
 *
 * Return: Nothing
 */
void reverse(listint_t **head, listint_t *prev, listint_t *node)
{
	if (node->next != NULL)
	{
		prev = node;
		node = node->next;
		*head = (*head)->next;
		reverse(head, prev, node);
		node->next = prev;
	}
}

/**
 * reverse_listint - reverses a linked list
 * @head: a list of elements with a pointer to the first element
 *
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *node;

	if (head == NULL || *head == NULL)
	{
		return (NULL);
	}
	node = *head;
	prev = node;
	reverse(head, prev, node);
	node->next = NULL;
	return (*head);
}

listint_t *copy_list(listint_t **head)
{
	listint_t *new = NULL, *ptr = *head;

	while (ptr != NULL)
	{
		add_nodeint_end(&new, ptr->n);
		ptr = ptr->next;
	}
	return (new);
}

int nElements(listint_t **head)
{
	int n = 0;
	listint_t *ptr = *head;

	while (ptr != NULL)
	{
		n++;
		ptr = ptr->next;
	}
	return (n);
}

int is_palindrome(listint_t **head)
{
	listint_t *rev, *ptr, *pRev;
	int i;

	if (head == NULL)
		return (1);
	ptr = *head;
	rev = copy_list(head);
	reverse_listint(&rev);
	pRev = rev;
	for (i = nElements(head) / 2; i > 0; i--)
	{
		if (pRev->n != ptr->n)
		{
			free_listint(rev);
			return (0);
		}
		pRev = pRev->next;
		ptr = ptr->next;
	}
	free_listint(rev);
	return (1);
}
