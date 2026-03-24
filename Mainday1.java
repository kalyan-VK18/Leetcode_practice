//Find maximum element in an array
import java.util.Scanner;
public class Mainday1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
            if(arr[i]>arr[0]){
                arr[0]=arr[i];
            }
        }
        System.out.println(arr[0]);
    }
}