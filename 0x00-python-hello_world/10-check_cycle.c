#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: List to be checked.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *iterator1 = list;
	listint_t *iterator2 = list;

	if (list == NULL)
		return (0);
	while (iterator2 != NULL && iterator2->next != NULL)
	{
		iterator2 = iterator2->next->next;
		iterator1 = iterator1->next;
		if (iterator1 == iterator2)
			return (1);
	}
	return (0);
}
