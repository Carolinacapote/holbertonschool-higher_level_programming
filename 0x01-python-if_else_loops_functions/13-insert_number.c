#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new_node, *prev_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	tmp = *head;
	while (tmp != NULL && tmp->n < new_node->n)
	{
		prev_node = tmp;
		tmp = tmp->next;
	}
	prev_node->next = new_node;
	new_node->next = tmp;
	return (new_node);
}
