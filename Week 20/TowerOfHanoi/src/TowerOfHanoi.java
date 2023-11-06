import java.lang.reflect.Array;
import java.util.Scanner;
import java.util.ArrayList;

public class TowerOfHanoi {
  String name;
  ArrayList[] peg;
  int numDiscs;

  public TowerOfHanoi(String name, int n) {
    this.name = name;
    this.numDiscs = n;
    this.peg = new ArrayList[3];
    // Write your code here
    ArrayList peg = new ArrayList();
    StringBuilder pegstr = new StringBuilder();
    for (int i = 0; i < n; i++) pegstr.append(" " + i);
    pegstr.append(" ");
    peg.add(pegstr);
    this.peg[0] = peg;

    ArrayList empty = new ArrayList();
    String blank = " ";
    empty.add(blank);
    for (int i = 1; i <= 2; i++) this.peg[i] = empty;
  }

  private void moveDisc(int src, int des) {
    // Write your code here
    String first_peg = peg[src].get(0).toString();
    char last_digit = first_peg.charAt(first_peg.length()-2);


    first_peg = first_peg.substring(0, first_peg.length()-2);
    ArrayList first = new ArrayList();
    first.add(first_peg);
    peg[src] = first;

    StringBuilder des_peg = new StringBuilder();
    des_peg.append(peg[des].get(0));
    des_peg.append(last_digit + " ");
    ArrayList dest = new ArrayList();
    dest.add(des_peg);
    peg[des] = dest;

    printTower();
  }

  public void printTower() {
    // Write your code here
    System.out.println(this.peg[0] + ", " + this.peg[1] + ", " + this.peg[2]);
  }

  public void makeMoves(int n, int src, int des, int aux) {
    if (n <= 0) return;
    makeMoves(n-1, src, aux, des);
    moveDisc(src, des);
    makeMoves(n-1, aux, des, src);
    return;
  }
  
  public static void main(String args[]) {
    Scanner input = new Scanner(System.in);
    System.out.println("Enter number of disks: ");
    int n = input.nextInt();
    TowerOfHanoi t = new TowerOfHanoi("Hanoi", n);
    t.printTower();
    t.makeMoves( n, 0, 2, 1 );
    StringBuilder test = new StringBuilder(" 1 2 3 ");
    System.out.println(test.charAt(2));
  }
  
}
  