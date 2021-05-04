#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - Inserts a new node in a sorted linked list.
 * @head: Double pointer to head.
 * @number: Value of the new node.
 * Return: The adress of the new node or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new_node, *prev_node;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	if ((*head)->n > new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
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
