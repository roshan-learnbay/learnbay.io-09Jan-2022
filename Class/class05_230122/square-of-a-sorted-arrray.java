//============================================================
    //Approach2, JAVA Solution
/*
public int[] sortedSquares(int[] nums)
{
    int low =0,high=nums.length-1;
    int[] res = new int[nums.length];
    int idx = nums.length-1;
    while(low<=high)
    {
        int lowSq = nums[low]*nums[low];
        int highSq = nums[high]*nums[high];
        if(lowSq<highSq)
        {
            res[idx--]=highSq;
            high--;
        }
        else
        {
            res[idx--] = lowSq;
            low++;
        }
    }
    return res;
}
*/

//=================================================================
// Java program to Sort square of
// the numbers of the array


import java.util.*;
import java.io.*;

//class GFG{

// Function to sort an square array
public static void sortSquares(int arr[])
{
	int n = arr.length, left = 0,
		right = n - 1;

	int result[] = new int[n];

	for(int index = n - 1; index >= 0; index--)
	{
		if (Math.abs(arr[left]) > arr[right])
		{
			result[index] = arr[left] * arr[left];
			left++;
		}
		else
		{
			result[index] = arr[right] * arr[right];
			right--;
		}
	}
	for(int i = 0; i < n; i++)
		arr[i] = result[i];
}

// Driver code
public static void main(String[] args)
{
	int arr[] = { -6, -3, -1, 2, 4, 5 };
	int n = arr.length;

	System.out.println("Before sort ");
	for(int i = 0; i < n; i++)
		System.out.print(arr[i] + " ");

	sortSquares(arr);
	System.out.println("");
	System.out.println("After Sort ");
	for(int i = 0; i < n; i++)
		System.out.print(arr[i] + " ");
}
//}

// This code is contributed by jinalparmar2382
