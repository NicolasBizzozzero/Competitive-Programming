#include <stdio.h>
#include <stdlib.h>

void solve_case(int casenr) {
  int n, pj, pg; scanf("%d%d%d", &n, &pj, &pg);
  int j=1; while(pj*j%100!=0) ++j;
  printf("Cas #%d: %s\n", casenr, j>n||pg==0&&pj>0||pg==100&&pj<100?"FAUX":"VRAI");
}

int main() {
  int C; scanf("%d",&C);
  int i; for(i=1; i<=C; i++) solve_case(i);
  return 0;
}
