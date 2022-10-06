#include <stdio.h>
#include <conio.h>
#include <string.h>

int main()
 {
	FILE *fp;
	int i,j,c,k,n;
	char a[100], stuff[200], dstuff[100], flag,e;
	flag='\0';
	e='\0';
	fp=fopen("byte.txt", "w");
	printf("Enter the String: ");
	gets(a);
	printf("\n Enter flag: ");
	scanf("%c",&flag);
	printf("\nEnter Stuffing char: ");
	e=getch();
	putch(e);
	stuff[0]=flag;
	c-0;
	//transferring into file
	fputs("Entered String: ", fp);
	fputs(a,fp);
	fputs("\nEntered flag: ", fp);
	fputc(flag,fp);
	fputs("\nEntered Stuffing Chae: ",fp);
	fputc(e,fp);
	fclose(fp);
	for(i=0,j=1;a[i]!='\0';i++,j++) {
		stuff[j]=a[i];
		if(a[i+1]==flag){
				j++;
				stuff[j]=e;	}}
	//disp
	printf("\n------------------------------");
	stuff[j]=flag;
	printf("\nStuffed string: ");
	for(i=0;i<=j;i++) {
		printf("%c", stuff[i]); }
	stuff[i]='\0';
	fp=fopen("byte.txt","a");
	fputs("\n", fp);
	fputs("\nStuffed string: ", fp);
	fputs(stuff,fp);
	//destuffing
	printf("\nDe-stuffed string: ");
	for(i=1,k=0;i<j;i++)
	{ if(stuff[i+1]==flag && stuff[i]==e)
		continue;
	else {
			dstuff[k]=stuff[i];
			k++;  }}
	dstuff[k]='\0';
	fputs("\n", fp);
	fputs("\nDe-stuffed byte: ", fp);
	fputs(dstuff,fp);
	fclose(fp);
	printf("%s", dstuff);
	getch();
}

