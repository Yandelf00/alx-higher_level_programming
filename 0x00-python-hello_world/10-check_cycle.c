#include "lists.h"

/**
 * check_cycle - finds the cycle in linkedlist
 * @list: head of list
 * Return: 1 if cycle and 0 if no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && (*fast).next)
	{
		slow = (*slow).next;
		fast = (*(*fast).next).next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
