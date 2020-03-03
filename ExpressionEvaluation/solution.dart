void main() {
  List operations = ['-', '+', '*', '/', '('];
  String operation = operations.removeLast();
  String s = '2+4/2*(7*4-2)';
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

      //if dividing
      if (operation == '/') {
        String leftVal = string[i - 1];
        String rightVal = string[i + 1];
        int left = int.tryParse(leftVal);
        int right = int.tryParse(rightVal);
        result = left / right;
      } 
      
      //multiply
      else if (operation == '*') {
        String leftVal = string[i - 1];
        String rightVal = string[i + 1];
        int left = int.tryParse(leftVal);
        int right = int.tryParse(rightVal);
        result = (left * right).toDouble();
      } 
      
      //add
      else if (operation == '+') {
        String leftVal = string[i - 1];
        String rightVal = string[i + 1];
        int left = int.tryParse(leftVal);
        int right = int.tryParse(rightVal);
        result = (left + right).toDouble();
      } 
      //subtract
      else if (operation == '-') {
        String leftVal = string[i - 1];
        String rightVal = string[i + 1];
        int left = int.tryParse(leftVal);
        int right = int.tryParse(rightVal);
        result = (left - right).toDouble();
      } 
      //bracket
      else if (operation == '(') {
        int index = getIndex(string, ')', i);
        String newString = string.substring(i + 1, index);
        List newOps = operations.map((element) => element).toList();
        newString = driver(newString, operation, newOps);
        print(newString);
        String ss = string.substring(i, index + 1);
        string = string.replaceAll(ss, newString);
      }

      //get the substrin to replace in string
      if (operation != '(') {
        String ss = string.substring(i - 1, i + 2);
        //replace the substring with the result as string
        string = string.replaceAll(ss, result.toString());
      }
    } //end if

  } //end for
  //operation = operations.removeLast();
  print(string);
  string = driver(string, operation = operations.removeLast(), operations);
  return string;
}

bool isNumeric(String s) {
  if (s == null) {
    return false;
  }
  if (double.tryParse("hello") != null) {
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

void printf(msg) {
  print(msg);
}
