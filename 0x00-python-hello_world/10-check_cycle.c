#include "lists.h"
/**
  *check_cycle - checks for a cycle in a linked list
  *@list: head of the linked list
  *Return: 1 if there is , 0 if not
  */

int check_cycle(listint_t *list)
{
	listint_t *head = list, *checker = list;
	int num = 0;

	if (!head)
		return (0);
	while (checker->next)
	{
		if (checker->next->next == NULL)
			return (0);
		checker = (checker->next)->next;
		head = head->next;
		if (head == checker)
		{
			num = 1;
			break;
		}
	}
	return (num);
}
