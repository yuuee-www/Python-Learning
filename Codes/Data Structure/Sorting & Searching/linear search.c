/* Linear search */

int linearSearch(int *a,int n,int key)
{
	int i;
	for(i=0;i<n&&a[i]!=key;i++);
	return(i<n?i:-1);
}
