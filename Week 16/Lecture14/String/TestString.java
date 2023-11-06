class TestString {

 public static void main(String[] args) {
  String text = "I'm studying CS1010X. ";

  System.out.println("text: " + text);
  System.out.println("text.length() = " + text.length());
  System.out.println("text.substring(5,8) = " + text.substring(5,8));

  System.out.println("text.indexOf(\"in\") = " + text.indexOf("in"));

  String newText = text + "How about you?";
  System.out.println("newText: " + newText);
  if (text.equals(newText))
   System.out.println(" text and newText are equal.");
  else
   System.out.println(" text and newText are not equal.");

 }
}
