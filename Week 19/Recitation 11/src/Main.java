import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {
        int[] test = {90,3,6,3,63,1};
        sorter(test);
    }

    public static int Fibbonaci(int n){
        int fib1 = 0;
        int fib2 = 1;
        for (int i = 0; i < n; i++){
            int temp = fib1 + fib2;
            fib1 = fib2;
            fib2 = temp;
        }
        return fib1;
    }

    static int[] coins = {1, 5, 10, 20, 50};

    static int counting_change(int amount, int kind_of_coins){
        if (amount < 0 || kind_of_coins <= 0) return 0;
        else if (amount == 0) return 1;
        return counting_change(amount-coins[kind_of_coins-1], kind_of_coins) +
                counting_change(amount, kind_of_coins-1);
    }

    static ArrayList[] split_array(int[] arr, int n) {
        ArrayList temp = new ArrayList<>();
        for (int i = 0; i < arr.length; i++){
            temp.add(arr[i]);
        }
        return split_array(temp, n);
    }
    static ArrayList[] split_array(ArrayList<Integer> arr, int n){
        ArrayList less_than_equal = new ArrayList<>();
        ArrayList more = new ArrayList<>();
        for (int i=0; i< arr.size(); i++){
            if (arr.get(i)<=n) less_than_equal.add(arr.get(i));
            else more.add(arr.get(i));
        }
        ArrayList[] res = {less_than_equal, more};
        return res;
    }

    static void sorter(int[] arr){
        if (arr.length == 1) return;
        int pivot = arr[0];
        ArrayList[] split = split_array(arr, pivot);
        System.out.println(split[0]);
    }
}

