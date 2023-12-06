/* Online Java Compiler and Editor */
public class ClassDemo{
     public static void main(String []args){
        // Array of type integeer
        /* 
        We can also specify arrays of other data types 
        */
        int[] nums={1,2,3,4,5,6,7,8,9,10};
        // System.out - is equivalent to print
        System.out.println("Hello, World!");
        // For loop example
        for(int i=0;i<10;i++){
            System.out.println("Hello World " + i);
        }
        System.out.println("---------");
        // For loop using the defined array
        for(int item=0;item<nums.length;item++){
            System.out.println("Count is: " + item);
        }
        System.out.println("---------");
     }
}