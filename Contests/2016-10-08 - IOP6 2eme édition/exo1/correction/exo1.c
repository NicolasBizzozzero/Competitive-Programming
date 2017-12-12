#include <stdio.h>
#include <stdlib.h>

/****** Corrigé sous forme noob-code pour faciliter la compréhension *****/

/* Données de l'énoncé */
//#define C_MAX 100
//#define S_MAX 1000
int C;
//char S[S_MAX+1];
FILE* input_file;

int main(int argc, char** argv)
{
  int i, j, k;  // compteurs
  int buff[26]; // va servir à compter les occurences de chaque lettre
  int res[10];  // buffer résultats: occurences de chaque chiffres
  char c;       // lectures lettre par lettre

  /* on prend en paramètre le nom du fichier à traiter */
  if(argc != 2){
    printf("Error: usage: %s <input_file>\n", argv[0]);
    return EXIT_FAILURE;
  }

  input_file = fopen(argv[1], "r");
  if(!input_file){
    printf("Error: cannot read file %s\n", argv[1]);
    return EXIT_FAILURE;
  }

  fscanf(input_file, "%d\n", &C);

  /* pour chaque cas d'utilisation */
  for(i=1; i<=C; i++){
    /* init */
    for(j=0; j<26; j++)
      buff[j] = 0;
    for(j=0; j<10; j++)
      res[j] = 0;

    /* lecture des lettres */
    while((c=getc(input_file)) != '\n' && c != EOF)
      buff[c-'A']++;

    /***** traitement buff[] -> res[] *****/

    /* On va virer les chiffres un par un */
    /* 1. ZERO => l'unique Z */
    if(buff['Z'-'A'] > 0){ // on pourrait se passer de ce test.
      buff['E'-'A'] -= buff['Z'-'A'];
      buff['R'-'A'] -= buff['Z'-'A'];
      buff['O'-'A'] -= buff['Z'-'A'];
      res[0] = buff['Z'-'A']; // on stocke le nombre d'occurences du chiffre
      buff['Z'-'A'] = 0;
    }
    /* 2. SEPT, l'unique P */
    if(buff['P'-'A'] > 0){
      buff['S'-'A'] -= buff['P'-'A'];
      buff['E'-'A'] -= buff['P'-'A'];
      buff['T'-'A'] -= buff['P'-'A'];
      res[7] = buff['P'-'A'];
      buff['P'-'A'] = 0;
    }
    /* 3. NEUF, l'unique F */
    if(buff['F'-'A'] > 0){
      buff['N'-'A'] -= buff['F'-'A'];
      buff['E'-'A'] -= buff['F'-'A'];
      buff['U'-'A'] -= buff['F'-'A'];
      res[9] = buff['F'-'A'];
      buff['F'-'A'] = 0;
    }
    /* 4. HUIT, l'unique H */
    if(buff['H'-'A'] > 0){
      buff['U'-'A'] -= buff['H'-'A'];
      buff['I'-'A'] -= buff['H'-'A'];
      buff['T'-'A'] -= buff['H'-'A'];
      res[8] = buff['H'-'A'];
      buff['H'-'A'] = 0;
    }
    /* 5. CINQ, l'unique C */
    if(buff['C'-'A'] > 0){
      buff['I'-'A'] -= buff['C'-'A'];
      buff['N'-'A'] -= buff['C'-'A'];
      buff['Q'-'A'] -= buff['C'-'A'];
      res[5] = buff['C'-'A'];
      buff['C'-'A'] = 0;
    }
    /* 6. QUATRE, les Q restants */
    if(buff['Q'-'A'] > 0){
      buff['U'-'A'] -= buff['Q'-'A'];
      buff['A'-'A'] -= buff['Q'-'A'];
      buff['T'-'A'] -= buff['Q'-'A'];
      buff['R'-'A'] -= buff['Q'-'A'];
      buff['E'-'A'] -= buff['Q'-'A'];
      res[4] = buff['Q'-'A'];
      buff['Q'-'A'] = 0;
    }
    /* 7. TROIS, les T restants */
    if(buff['T'-'A'] > 0){
      buff['R'-'A'] -= buff['T'-'A'];
      buff['O'-'A'] -= buff['T'-'A'];
      buff['I'-'A'] -= buff['T'-'A'];
      buff['S'-'A'] -= buff['T'-'A'];
      res[3] = buff['T'-'A'];
      buff['T'-'A'] = 0;
    }
    /* 8. SIX, les S restants */
    if(buff['S'-'A'] > 0){
      buff['I'-'A'] -= buff['S'-'A'];
      buff['X'-'A'] -= buff['S'-'A'];
      res[6] = buff['S'-'A'];
      buff['S'-'A'] = 0;
    }
    /* 9. DEUX, l'unique D */
    if(buff['D'-'A'] > 0){
      buff['E'-'A'] -= buff['D'-'A'];
      buff['U'-'A'] -= buff['D'-'A'];
      buff['X'-'A'] -= buff['D'-'A'];
      res[2] = buff['D'-'A'];
      buff['D'-'A'] = 0;
    }
    /* 10. UN, les U ou N restants */
    res[1] = buff['U'-'A'];

    /* affichage du résultat pour ce cas d'utilisation */
    printf("Cas #%d: ", i);
    for(j=0; j<10; j++)
      for(k=0; k<res[j]; k++)
	printf("%d", j);
    printf("\n");
  }

  fclose(input_file);

  return EXIT_SUCCESS;
}
