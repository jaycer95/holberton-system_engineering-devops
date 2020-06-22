#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
/**
 * infinite_while - function to use after creating parent and zombie process
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main -  creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	int i = 1;

	while (i <= 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
			exit(0);
		i++;
	}
	infinite_while();
	return (0);
}
