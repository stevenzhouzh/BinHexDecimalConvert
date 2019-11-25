#include <stack>
#include <iostream>
using namespace std;
long long fastpower(int base, int power)
{
    long long result = 1;
    while (power > 0) {
        if (power & 1) {
            result=result*base;
        }
        power >>= 1;
        base = (base * base);
    }
    return result;
}
int main()
{
  stack<int> input;
  string func1,func2;
  cin>>func1>>func2;
  char tmp;
  int count=0;
  cin>>tmp;
  long long answer=0;
  while (tmp!=q) {
    if (tmp>=48 && tmp<=57) {
      tmp-=48;
    }
    if (tmp>='a' && tmp<='f') {
      tmp-=('a'-10);
    }
    input.push(tmp);
    count++;
    tmp=getchar();
  }
  // All->dec
  if (func1 == hex) {
    for (i=1;i<=count;i++) {
      long long tmp = fastpower(16,count);
      answer+=(tmp*input.top());
      count--;
      input.pop();
    }
  }
  if (func1 == dec) {
    for (i=1;i<=count;i++) {
      long long tmp = fastpower(10,count);
      answer+=(tmp*input.top());
      count--;
      input.pop();
    }
  }
  if (func1 == oct) {
    for (i=1;i<=count;i++) {
      long long tmp = fastpower(8,count);
      answer+=(tmp*input.top());
      count--;
      input.pop();
    }
  }
  if (func1 == bin) {
    for (i=1;i<=count;i++) {
      long long tmp = fastpower(2,count);
      answer+=(tmp*input.top());
      count--;
      input.pop();
    }
  }
  // Dec->All coming...
  return 0;
}
