#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
   char a[100],ack;
	int l,wsize,i,j,nnack,f[10],start,nack,k;
	printf("Enter Data Stream: "); //got data from user
	gets(a);
   	printf("Enter Window size: "); //got ws 
	scanf (" %d" ,&wsize);
	 printf("(Please press 'Y' n 'N' Accordingly)\n");
		 l=strlen(a); 
		 printf ("\n\n\t"); 
		for (i=0;i<l;i++) 
		 printf("%d ",i);
		printf("\n\t");
		for (i=0;i<l;i++)
		printf("%c ",a[i]);
printf("\n\nSENDER SIDE\t |Y| \tRECEIVER SIDE\t|Ack Number\n-------------------------------------------------------------");
start=0;
while (start<l)
{
nnack=0;
for(i =start;i<start+wsize && i<l;i++)
{
printf("\n\nSEND %c\t",a[i]);
ack=getch();
if(ack == 'y' || ack=='Y'){
printf("\t|%c|\tReceived %c\t|\t%d" ,ack,a[i],i);
}
if(ack=='n' || ack=='N')
{
 f[nnack++]=i;
 printf("\t|%c|\tNot Received \t|\t%d",ack,i);
}
}
if(nnack!=0){
printf("\n\n\tNegative Acknowledgement Number : ");
for (j=0;j<nnack;j++){
printf("%d ",f[j]);
}
do{
for(j=0,k=0;j<nnack;j++) {
printf("\n\nResending %c",a[f[j]]);
ack=getch();
if(ack=='N' || ack=='n')
 {
f[k]=f[j];
k++;
printf("\t|%c|\tNot Received \t|\t%d",ack,f[j]);
}
else
 printf("\t|%c|\tReceived %c\t|\t%d", ack ,a[f[j]],f[j]);
 }
 nnack=k;
 }
while(k>0);
}
 else if (i < l) 
 {
 printf("\t\t\t\t\t\t\tACK : %d" ,i);
 }
 start=i;
}
printf("\n\n Data Stream Received: %s\n\n" ,a);
}



