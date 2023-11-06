import java.util.*;
public class VehiclePlate {
 
   public static void main(String[] args) {

      Scanner stdIn = new Scanner(System.in);

      System.out.print("Vehicle Plate (excluding the checksum alphabet at the end): ");
      String plate = stdIn.nextLine();
      plate = plate.toUpperCase();
      String prefix =  plate.replaceAll("[0123456789]", "");
      int suffix = Integer.parseInt(plate.replaceAll("[a-zA-Z]",""));
      char checkSum = generateCheckSum (prefix, suffix);

      System.out.println("Vehicle Plate is: " + prefix + " " + suffix + " " + checkSum);

   } // end main

   /*********************************************************
      
   **********************************************************/
   public static char generateCheckSum(String prefix, int suffix) {
      /*StringBuilder nums = new StringBuilder();
      if (prefix.length() == 1) nums.append("00");
      else if (prefix.length() > 2) prefix = prefix.substring(1);
      for (int i = 0; i < prefix.length(); i++){
         int num = prefix.charAt(i) - 'A' + 1;
         String StrNum;
         if (num < 10) StrNum = "0" + num;
         else {
            StrNum = String.valueOf(num);
         }
         nums.append(StrNum);
      }
      String StrSuff = String.valueOf(suffix);
      int StrSuffLen = StrSuff.length();
      nums.append("00".repeat(4-StrSuffLen));
      for (int i = 0; i < StrSuffLen; i++) nums.append("0" + StrSuff.charAt(i));
      int checksumnum = 0;
      System.out.println("nums = " + nums);
      for (int i = 0; i < nums.length(); i = i+2){
         int currnum = 10*(nums.charAt(i)-'0') + nums.charAt(i+1) - '0';
         switch (i){
            case 0:
               checksumnum += currnum * 9;
               break;
            case 2:
            case 6:
               checksumnum += currnum * 4;
               break;
            case 4:
               checksumnum += currnum * 5;
               break;
            case 8:
               checksumnum += currnum * 3;
               break;
            case 10:
               checksumnum += currnum * 2;
               break;
         }
      }
      char[] tally = {'A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M', 'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B'};
      return tally[(checksumnum%19)];*/
      int[] numbers = new int[6];
      int n = prefix.length();
      if (n==1) numbers[0] = 0;
      else numbers[0] = (prefix.charAt(n-2) - 'A' + 1)*9;
      numbers[1] = (prefix.charAt(n-1) - 'A' + 1)*4;
      String suff = Integer.toString(suffix);

      int[] multiplier = {5,4,3,2};
      for (int i = 1; i < suff.length() + 1; i++){
         numbers[numbers.length-i] = (suff.charAt(suff.length()-i) - '0')*multiplier[multiplier.length-i];
      }
      int sum = 0;
      for (int i = 0; i < numbers.length; i++){
         sum += numbers[i];
      }
      char[] tally = {'A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M', 'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B'};
      return tally[(sum%19)];
   }// end generateCheckSum

}// end class 