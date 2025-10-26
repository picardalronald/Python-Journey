// print out unique characters from a string using built-in array-unique function or it's equivalent

public class day17 {
    public static void main(String[] args) {
     
     String text = "programming";
     text = text.toLowerCase();


      for (int i = 0; i < text.length(); i++){
      char ch = text.charAt(i);
      if(text.indexOf(ch) == text.lastIndexOf(ch)){
      
        System.out.println(ch + "");

    }
     }


    }
}

                  
