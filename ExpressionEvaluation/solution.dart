void main() {
  List operations = ['-', '+', '*', '/', '('];
  String operation = operations.removeLast();
  String s = "3*3*3*3*(8/7.5)-5";
  s = driver(s, operation, operations);
  print(s);
}

String driver(string, operation, List operations) {
  //if all operations have been completed return
  if (isNumeric(string)) {
    return string;
  }

  //go through the string and fin all occurrences of the operation
  for (int i = 0; i < string.length; i++) {
    //if the operation is found then
    if (string[i] == operation) {
      //get the left val

      //result is the result of the operation
      double result = -1;

      int leftIndex = getLeftIndex(string, i-1);
      int rightIndex = getRightIndx(string, i+1); 
      String leftVal = string.substring(leftIndex, i);
      String rightVal = string.substring(i+1, rightIndex+1);
      double left = double.tryParse(leftVal);
      double right = double.tryParse(rightVal);
      //if dividing
      if (operation == '/') {

        result = left / right.toDouble();
      } 
      
      //multiply
      else if (operation == '*') {

        result = (left * right).toDouble();
      } 
      
      //add
      else if (operation == '+') {
        
        result = (left + right).toDouble();
      } 
      //subtract
      else if (operation == '-') {
        result = (left - right).toDouble();
      } 
      //bracket
      else if (operation == '(') {
        int index = getIndex(string, ')', i);
        String newString = string.substring(i + 1, index);
        List newOps = operations.map((element) => element).toList();
        newString = driver(newString, operation, newOps);
        String ss = string.substring(i, index + 1);
        string = string.replaceAll(ss, newString);
      }

      //get the substrin to replace in string
      if (operation != '(') {
        String ss = string.substring(leftIndex, rightIndex+1);
        //replace the substring with the result as string
        string = string.replaceAll(ss, result.toString());
      }
    } //end if

  } //end for

  if(!(operations.isEmpty)){
    operation = operations.removeLast();
    string = driver(string, operation, operations);
  }
  return string;
}


int getLeftIndex(String s, int start)
{
  for(int i = start; i >=0; i--)
  {
    if(!(s.codeUnitAt(i) ^ 0x30 <= 9) && !(s[i] == '.'))
    {
      return i+1;
    }
  }
  return 0;
}

int getRightIndx(String s, int start)
{

  for(int i = start; i < s.length; i++)
  {
    if(!(s.codeUnitAt(i) ^ 0x30 <= 9) && !(s[i] == '.'))
    {
      return i-1;
    }
  }
   return s.length-1;
  
 }

bool isNumeric(String s) {
  if (s == null) {
    return false;
  }
  if (double.tryParse(s) != null) {
    return true;
  } else {
    return false;
  }
}

int getIndex(String s, String char, int start) {
  for (int i = start; i < s.length; i++) {
    if (s[i] == char) {
      return i;
    }
  }
  return -1;
}



