
import java.io.*; 

class  Assgnmnt1 
{ 
    // Creating the matrix
    static void lcs(String X, String Y, int m, int n) 
    { 
        int[][] L = new int[m+1][n+1]; 
   
        // Following steps build L[m+1][n+1] in bottom up fashion.   
        for (int i=0; i<=m; i++) 
        { 
            for (int j=0; j<=n; j++) 
            { 
                if (i == 0 || j == 0) 
                    L[i][j] = 0; 
                else if (X.charAt(i-1) == Y.charAt(j-1)) 
                    L[i][j] = L[i-1][j-1] + 1; 
                else
                    L[i][j] = Math.max(L[i-1][j], L[i][j-1]); 
            } 
        } 
    
        int index = L[m][n]; 
        int temp = index; 
   
        // Create a character array to store the lcs string 
        char[] lcs = new char[index+1]; 
        lcs[index] = ' '; // Set the terminating character 
   
        // Start from the right-most-bottom-most corner and 
        // one by one store characters in lcs[] 
        int i = m, j = n; 
        while (i > 0 && j > 0) 
        { 
             
            if (X.charAt(i-1) == Y.charAt(j-1)) 
            { 
                // Put current character in result 
                lcs[index-1] = X.charAt(i-1);  
                  
                // reduce values of i, j and index 
                i--;  
                j--;  
                index--;      
            } 
   
            // If not same, then find the larger of two and 
            // go in the direction of larger value 
            else if (L[i-1][j] > L[i][j-1]) 
                i--; 
            else
                j--; 
        } 
   
        // Print the lcs 
        System.out.print("LCS of "+X+" and "+Y+" is "); 
        for(int k=0;k<=temp;k++) 
            System.out.print(lcs[k]); 
    } 
      
    // driver program 
    public static void main (String[] args)  
    { 
        String X = "ABCDGH"; 
        String Y = "AEDFHR"; 
        int m = X.length(); 
        int n = Y.length(); 
        lcs(X, Y, m, n); 
    } 
} 