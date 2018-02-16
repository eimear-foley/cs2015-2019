/**
Date: 24th January 2018
Author: Eimear Foley
Student ID: 115352866
*/
#include <stdio.h>
#include <stdlib.h>

int main() {

	//Length of outer array i.e. first line of file
	int array_len;
	scanf("%d", &array_len);
	//Intialisation of 2D-array using 'array_len' length
	int *array[array_len];
	//Points to current line of file
	int line = 0;
	//Points to next integer value along the line
	int counter = 0;
	//Keeps track of index of 2D-array
	int index;

	//While not at end of file
	while ((scanf("%d", &array_len) != EOF)) {
		index = 0;
		if (array_len != '\n') {
			counter = array_len;
			//create array equal to size of first int on each line of file
			array[line] = malloc(sizeof(int) * counter);

			//Store remaining values of line into just created array
			for (int i=0; i < counter; i++) {
				scanf("%d", &array_len);
				array[line][index] = array_len;
				index++;
			}
			line++;
		}
	}
}