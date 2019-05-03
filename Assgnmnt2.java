public class Assgnmnt2 {

    /**
     * Dynamic programming technique using Matrix method.
     */
    public boolean matchRegex(char[] text, char[] pattern) {
        boolean T[][] = new boolean[text.length + 1][pattern.length + 1];

		
        T[0][0] = true;
        //Deals with patterns like a* or a*b* or a*b*c* 
		  for (int i = 1; i < T[0].length; i++) { if (pattern[i-1] == '*') { T[0][i] =
		  T[0][i - 2]; } }
		 
		 
		  //Initialize the whole matrix to false
		  for (int i = 1; i < T.length; i++) {
	            for (int j = 1; j < T[i].length; j++) {
	            	T[i][j]=false;
	            }
		  }  
		    
		         
        for (int i = 1; i < T.length; i++) {
            for (int j = 1; j < T[i].length; j++) {
                if (pattern[j - 1] == '.' || pattern[j - 1] == text[i - 1]) {
                    T[i][j] = T[i-1][j-1];
                } else if (pattern[j - 1] == '*')  {
                    if (pattern[j-2] == '.' || pattern[j - 2] == text[i - 1]) {
                        T[i][j] = T[i][j-1] | T[i - 1][j];
                    }
                } else {
                    T[i][j] = false;
                }
            }
        }
        return T[text.length][pattern.length];
    }

    public static void main(String args[]){
        Assgnmnt2 rm = new Assgnmnt2();
        System.out.println(rm.matchRegex("aab".toCharArray(),"c*a*b".toCharArray()));
        System.out.println(rm.matchRegex("ab".toCharArray(),".*".toCharArray()));
		System.out.println(rm.matchRegex("aba".toCharArray(),"".toCharArray()));
		System.out.println(rm.matchRegex("ab".toCharArray(),".".toCharArray()));
		System.out.println(rm.matchRegex("aaa".toCharArray(),"a*".toCharArray()));
		System.out.println(rm.matchRegex("aa".toCharArray(), "a*".toCharArray()));
		 
    }
}