#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <fstream>
#include <sstream>
#include <ctime>
#include <cstdint>
#include "gzstream.h"

using namespace std;


#ifdef __linux__


string ANSI_RESET = "\x1b[0m";
string ANSI_BLACK = "\x1b[30m";
string ANSI_DARK_RED = "\x1b[31m";
string ANSI_DARK_GREEN = "\x1b[32m";
string ANSI_GOLD = "\x1b[33m";
string ANSI_DARK_BLUE = "\x1b[34m";
string ANSI_DARK_PURPLE = "\x1b[35m";
string ANSI_DARK_AQUA = "\x1b[36m";
string ANSI_GRAY = "\x1b[37m";
string ANSI_DARK_GRAY = "\x1b[30;1m";
string ANSI_RED = "\x1b[31;1m";
string ANSI_GREEN = "\x1b[32;1m";
string ANSI_YELLOW = "\x1b[33;1m";
string ANSI_BLUE = "\x1b[34;1m";
string ANSI_LIGHT_PURPLE = "\x1b[35;1m";
string ANSI_AQUA = "\x1b[36;1m";
string ANSI_WHITE = "\x1b[37;1m";
string ANSI_BOLD = "\x1b[1m";
string ANSI_CLEAR_SCREEN = "\x1b[2J\x1b[1;1H";

string ANSI_PIZZA_FREE = ANSI_RESET + "\x1b[47m" + ANSI_BLACK;
string ANSI_PIZZA_UNAVAILABLE = ANSI_RESET + "\x1b[41m" + ANSI_RED;

string partsColors[] = {
	ANSI_RESET + ANSI_DARK_RED,
	ANSI_RESET + ANSI_DARK_GREEN,
	ANSI_RESET + ANSI_GOLD,
	ANSI_RESET + ANSI_DARK_BLUE,
	ANSI_RESET + ANSI_DARK_PURPLE,
	ANSI_RESET + ANSI_DARK_AQUA,
	ANSI_RESET + ANSI_GRAY,
	ANSI_RESET + ANSI_DARK_GRAY,
	ANSI_RESET + ANSI_RED,
	ANSI_RESET + ANSI_GREEN,
	ANSI_RESET + ANSI_YELLOW,
	ANSI_RESET + ANSI_BLUE,
	ANSI_RESET + ANSI_LIGHT_PURPLE,
	ANSI_RESET + ANSI_AQUA
};
int nbPartsColors = 14;
#endif

typedef struct Point {
	int x, y;
} Point;





int previousExecBest;



/*
	Structure de données PartRoyale
*/
typedef struct PartRoyale {
	int index;
	int xMin;
	int xMax;
	int yMin;
	int yMax;
	PartRoyale(int index_, int xMin_, int xMax_, int yMin_, int yMax_) : index(index_), xMin(xMin_), xMax(xMax_), yMin(yMin_), yMax(yMax_) { }
	
	void print(ostream& out) const {
		out << yMin << " " << xMin << " " << yMax << " " << xMax << endl;
	}
	
	int getArea() const {
		return (xMax - xMin + 1) * (yMax - yMin + 1);
	}
	
	#ifdef __linux__
	string getColor() const {
		return partsColors[(xMin + yMin + xMax + yMax) % nbPartsColors];
	}
	#endif
	
	bool collideWith(PartRoyale& o) {
		return !(xMin > o.xMax || xMax < o.xMin || yMin > o.yMax || yMax < o.yMin);
	}
	
	float getCenterX() const {
		return (xMin + xMax) / 2.0;
	}
	float getCenterY() const {
		return (yMin + yMax) / 2.0;
	}
	
	static PartRoyale UNDEFINED;
	
	static bool compareByCenterPosition(const PartRoyale p1, const PartRoyale p2) {
		float y1 = p1.getCenterY();
		float y2 = p2.getCenterY();
		if (y1 == y2)
			return (p1.getCenterX() < p2.getCenterX());
		return (y1 < y2);
	}
} PartRoyale;
PartRoyale PartRoyale::UNDEFINED(-1, -1, -1, -1, -1);

inline bool operator==(const PartRoyale& p1, const PartRoyale& p2){ return (p1.xMin == p2.xMin && p1.xMax == p2.xMax && p1.yMin == p2.yMin && p1.yMax == p2.yMax); }
inline bool operator!=(const PartRoyale& p1, const PartRoyale& p2){ return !(p1 == p2); }

/*
	Structure de données Pizza
*/
typedef struct Pizza {
	int height, width, ham, maxRoyale;
	vector<vector<bool> >* matriceHam;
	vector<vector<bool> >* matriceCanPut;
	vector<vector<PartRoyale> > matriceFilled;
	vector<PartRoyale> parts;
	vector<PartRoyale>* possibleParts;
	vector<vector<vector<int> > >* matriceCollision;
	int numberFilled;
	int numberMax;
	int numberHam;
	
	/*
	Pizza(const Pizza& copied) {
		height = copied.height;
		width = copied.width;
		ham = copied.ham;
		maxRoyale = copied.maxRoyale;
		matriceHam = copied.matriceHam;
		matriceFilled = copied.matriceFilled;
		parts = copied.parts;
		numberFilled = copied.numberFilled;
		numberMax = copied.numberMax;
	}*/
	
	Pizza(istream& in, bool (*partRoyaleComp)(PartRoyale, PartRoyale)) : numberFilled(0) {
		in >> height >> width >> ham >> maxRoyale;
		
		numberMax = height * width;
		
		matriceCanPut = new vector<vector<bool> >();
		possibleParts = new vector<PartRoyale>();
		matriceHam = new vector<vector<bool> >();
		matriceCollision = new vector<vector<vector<int> > >();
		
		for (int i=0; i<height ; i++) {
			vector<bool> ligneJambon;
			vector<bool> lignePut;
			vector<vector<int> > ligneCollision;
			vector<PartRoyale> ligneFilled;
			for (int j=0; j<width; j++) {
				char ch;
				in >> ch;
				bool ham = ch == 'H';
				if (ham) numberHam++;
				ligneJambon.push_back(ham);
				lignePut.push_back(false);
				ligneCollision.push_back(vector<int>());
				ligneFilled.push_back(PartRoyale::UNDEFINED);
			}
			
			matriceHam->push_back(ligneJambon);
			matriceCanPut->push_back(lignePut);
			matriceCollision->push_back(ligneCollision);
			matriceFilled.push_back(ligneFilled);
		}
		
		for (int y = 0; y < height; y++) {
			for (int x = 0; x < width; x++) {
				for (int w = 1; w <= maxRoyale; w++) {
					for (int h = 1; w*h <= maxRoyale; h++) {
						PartRoyale el(0, x, x + w - 1, y, y + h - 1);
						if (canPut(el, true)) {
							possibleParts->push_back(el);
							for (int xP = el.xMin; xP <= el.xMax; xP++) {
								for (int yP = el.yMin; yP <= el.yMax; yP++) {
									(*matriceCanPut)[yP][xP] = true;
								}
							}
						}
					}
				}
			}
		}
		sort(possibleParts->begin(), possibleParts->end(), partRoyaleComp);
		for (int i = 0; i < possibleParts->size(); i++) {
			(*possibleParts)[i].index = i;
			PartRoyale el = (*possibleParts)[i];
			for (int xP = el.xMin; xP <= el.xMax; xP++) {
				for (int yP = el.yMin; yP <= el.yMax; yP++) {
					(*matriceCollision)[yP][xP].push_back(i);
				}
			}
		}
		
		for (int y = 0; y < height; y++) {
			for (int x = 0; x < width; x++) {
				if (!(*matriceCanPut)[y][x])
					numberMax--;
			}
		}
		
		
	}
	
	
	
	void fillWithInput(istream& in) {
		int nbPart;
		in >> nbPart;
		for (int i = 0; i < nbPart; i++) {
			PartRoyale part = PartRoyale::UNDEFINED;
			in >> part.yMin >> part.xMin >> part.yMax >> part.xMax;
			put(part);
		}
	}
	
	
	
	
	bool basicCheckPart(const PartRoyale&el) {
		if (el.xMax < el.xMin || el.yMax < el.yMin
			|| (el.xMax - el.xMin + 1) * (el.yMax - el.yMin + 1) > maxRoyale
			|| el.xMin < 0 || el.yMin < 0 || el.xMax >= width || el.yMax >= height)
			return false;
		return true;
	}
	
	
	bool canPut(const PartRoyale& el, bool ignoreFilled) {
		if (!basicCheckPart(el)) return false;
		
		int nbJambon = 0;
		for (int x = el.xMin; x <= el.xMax; x++) {
			for (int y = el.yMin; y <= el.yMax; y++) {
				if (!ignoreFilled && ((matriceFilled[y][x]) != PartRoyale::UNDEFINED))
					return false;
				if ((*matriceHam)[y][x])
					nbJambon++;
			}
		}
		
		return (nbJambon >= ham);
	}
	
	bool canPutInSubPizza(const PartRoyale& el, bool ignoreFilled, int firstLine, int nbLine) {
		if (el.yMin < firstLine || el.yMax >= firstLine + nbLine) return false;
		return canPut(el, ignoreFilled);
	}
	
	/*
		put a new PartRoyale in this Pizza structure.
		May remove interfering PartRoyale currently in
		this Pizza.
	*/
	void put(const PartRoyale el) {
		if (!basicCheckPart(el)) return;
		
		for (int x = el.xMin; x <= el.xMax; x++) {
			for (int y = el.yMin; y <= el.yMax; y++) {
				if (matriceFilled[y][x] != PartRoyale::UNDEFINED) {
					if (!remove(matriceFilled[y][x])) {
						cerr << "Can't remove PartRoyale ";
						matriceFilled[y][x].print(cerr);
						cerr << "When placing PartRoyale ";
						el.print(cerr);
						return;
					}
				}
			}
		}
		
		
		for (int x = el.xMin; x <= el.xMax; x++) {
			for (int y = el.yMin; y <= el.yMax; y++) {
				
				matriceFilled[y][x] = el;
				numberFilled++;
			}
		}
		parts.push_back(el);
		// cerr << "put -> " << numberFilled << endl;
	}
	
	int numberFilledInRange(int firstLine, int nbLine) {
		int c = 0;
		for (int x = 0; x < width; x++) {
			for (int y = firstLine; y < firstLine + nbLine; y++) {
				if (matriceFilled[y][x] != PartRoyale::UNDEFINED)
					c++;
			}
		}
		return c;
	}
	
	
	/*
		remove the PartRoyale at the specified index from
		the vector of PartRoyale of this Pizza
	*/
	/*
	PartRoyale remove(int i) {
		if (i<0 || i>=parts.size()) return PartRoyale::UNDEFINED;
		PartRoyale el = parts[i];
		parts.erase(parts.begin() + i);
		for (int x = el.xMin; x <= el.xMax; x++) {
			for (int y = el.yMin; y <= el.yMax; y++) {
				matriceFilled[y][x] = PartRoyale::UNDEFINED;
				numberFilled--;
			}
		}
		cerr << "Removed PartRoyale ";
		el.print(cerr);
		return el;
	}*/
	
	/*
		remove the specified PartRoyale from this Pizza
	*/
	bool remove(PartRoyale el) {
		if (!basicCheckPart(el)) return true;
		vector<PartRoyale>::iterator pos = find_if(parts.begin(), parts.end(), [el](PartRoyale& f){
			return f == el;
		});
		if (pos == parts.end()) return false;
		parts.erase(pos);
		for (int x = el.xMin; x <= el.xMax; x++) {
			for (int y = el.yMin; y <= el.yMax; y++) {
				matriceFilled[y][x] = PartRoyale::UNDEFINED;
				numberFilled--;
			}
		}
		return true;
	}
	
	
	
	
	void outputResult(ostream& out) {
		out << parts.size() << endl;
		for (int i = 0; i < parts.size(); i++) {
			parts[i].print(out);
		}
	}
	
	
	
	void outputToFile() {
		if (numberFilled <= previousExecBest)
			return;
		stringstream ss; ss << numberFilled;
		ofstream ofs("result"+ss.str()+".out", ofstream::out);
		outputResult(ofs);
		ofs.close();
		
		ofstream ofi("result"+ss.str()+".ppm", ofstream::out);
		displayPPM(ofi);
		ofi.close();
		
		ofstream ofb("best.txt", ofstream::out);
		ofb << numberFilled << endl;
		ofb.close();
	}
	
	
	void displayPizza(ostream& out) {
		#ifdef __linux__
		
		string previousColor = ANSI_PIZZA_FREE;
		out << ANSI_PIZZA_FREE;
		
		#endif
		for (int r = 0; r < height; r++) {
			for (int c = 0; c < width; c++) {
				#ifdef __linux__
				string currentColor = (matriceFilled[r][c] != PartRoyale::UNDEFINED)
						? matriceFilled[r][c].getColor() : ((*matriceCanPut)[r][c]) ? ANSI_PIZZA_FREE : ANSI_PIZZA_UNAVAILABLE;
				
				if (currentColor != previousColor) {
					out << currentColor;
					previousColor = currentColor;
				}
				#endif
				
				out << ((*matriceHam)[r][c] ? "H" : "T");
			}
			#ifdef __linux__
			out << ANSI_RESET;
			#endif
			out << endl;
			#ifdef __linux__
			out << previousColor;
			#endif
		}
		#ifdef __linux__
		out << ANSI_RESET;
		#endif
		out << "Nombre de points : " << numberFilled << endl;
		out << "Score max : " << numberMax << endl;
	}
	
	
	void displayPPM(ostream& out) {
		typedef struct {unsigned int x, y, z;} Color;
		Color FREE = {255, 255, 255};
		Color FREE_HAM = {255, 128, 255};
		Color FILLED = {64, 64, 64};
		Color FILLED_HAM = {64, 0, 64};
		Color UNAVAILABLE = {0, 0, 0};
		
		out << "P3 " << width << " " << height << " 255" << endl;
		
		for (int r = 0; r < height; r++) {
			for (int c = 0; c < width; c++) {
				Color currentColor = (matriceFilled[r][c] != PartRoyale::UNDEFINED)
						? ((*matriceHam)[r][c] ? FILLED_HAM : FILLED)
						: (*matriceCanPut)[r][c]
								? ((*matriceHam)[r][c] ? FREE_HAM : FREE)
								: UNAVAILABLE;
				
				out << currentColor.x << " " << currentColor.y << " " << currentColor.z << endl;
			}
		}
	}
	
	
	Point getFirstFreePoint() {
		Point p;
		for (int r = 0; r < height; r++) {
			for (int c = 0; c < width; c++) {
				if (matriceFilled[r][c] == PartRoyale::UNDEFINED) {
					p.x = c; p.y = r;
					return p;
				}
			}
		}
		p.x = -1; p.y = -1;
		return p;
	}
	
	
	
	bool isChunkFull(int xMin, int xMax, int yMin, int yMax) {
		for (int x = xMin; x <= xMax; x++) {
			for (int y = yMin; y <= yMax; y++) {
				if (matriceFilled[y][x] == PartRoyale::UNDEFINED && (*matriceCanPut)[y][x]) {
					return false;
				}
			}
		}
		return true;
	}
	
	void cleanChunk(bool inner, int xMin, int xMax, int yMin, int yMax) {
		for (int x = xMin; x <= xMax; x++) {
			for (int y = yMin; y <= yMax; y++) {
				PartRoyale part = matriceFilled[y][x];
				if (inner && (part.xMin < xMin || part.xMax > xMax
					|| part.yMin < yMin ||part.yMax > yMax))
					continue;
				remove(part);
			}
		}
	}
	
	
} Pizza;











Pizza* bestPizza;




void recursiveFill(Pizza& pizza, const vector<PartRoyale>& possibleParts, const vector<PartRoyale>::iterator start, int firstLine, int nbLine) {
	
	for (vector<PartRoyale>::iterator it = start; it != possibleParts.end(); ++it) {
		if (pizza.canPutInSubPizza(*it, false, firstLine, nbLine)) {
			pizza.put(*it);
			recursiveFill(pizza, possibleParts, it + 1, firstLine, nbLine);
			pizza.remove(*it);
		}
		
	}
	
	if (pizza.numberFilled > bestPizza->numberFilled) {
		cerr << "Nouveau score : " << pizza.numberFilled << endl;
		pizza.outputToFile();
		*bestPizza = pizza;
	}
	
}




void exactFill(Pizza& pizza, vector<PartRoyale>& possibleParts, int firstLine, int nbLine) {
	
	recursiveFill(pizza, possibleParts, possibleParts.begin(), firstLine, nbLine);
	
}





void linearFill(Pizza& pizza, vector<PartRoyale>& possibleParts) {
	cerr << "Linear solving: creating lp file..." << endl;
	// écriture du fichier d'entrée de GLPK
	ofstream of("glpk_in.lp", ofstream::out);
	of << "Maximize" << endl << "  obj: ";
	for (vector<PartRoyale>::iterator it = possibleParts.begin(); it != possibleParts.end(); ++it) {
		of << " +" << (*it).getArea() << " x" << (*it).index;
	}
	of << endl << "Subject To" << endl;
	for (int r = 0; r < pizza.height; r++) {
		for (int c = 0; c < pizza.width; c++) {
			stringstream ss;
			bool atLeastOne = false;
			for (int i = 0; i < (*(pizza.matriceCollision))[r][c].size(); i++) {
				int indexPart = (*(pizza.matriceCollision))[r][c][i];
				if (find(possibleParts.begin(), possibleParts.end(), (*(pizza.possibleParts))[indexPart]) != possibleParts.end()) {
					ss << " +x" << indexPart;
					atLeastOne = true;
				}
			}
			if (atLeastOne) {
				of << "  c" << r << "_" << c << ": " << ss.str() << " <= 1" << endl;
			}
		}
	}
	of << "Binary" << endl;
	for (vector<PartRoyale>::iterator it = possibleParts.begin(); it != possibleParts.end(); ++it) {
		of << " x" << (*it).index << endl;
	}
	of << "End" << endl;
	of.close();
	cerr << "Linear solving: running glpsol..." << endl;
	#ifdef __linux__
	
	#else
		system("\"glpk-4.60\\w64\\glpsol.exe\" --lp --exact -w glpk_out.mip glpk_in.lp");
	#endif
	cerr << "Linear solving: glpsol ended" << endl;
	
	cerr << "Linear solving: reading slpk_out.mip" << endl;
	ifstream ifs("glpk_out.mip", ifstream::in);
	if (!ifs.good()) {
		cerr << "Linear solving: can't read output file" << endl;
		return;
	}
	char line[256];
	do {
		ifs.getline(line, 256);
	} while (string(line) != string("c"));
	
	string s1; // inutile sauf pour passer les tokens
	int nbI, nbJ, score;
	ifs >> s1 >> s1 >> nbI >> nbJ >> s1 >> score;
	for (int i = 0; i < nbI; i++) ifs >> s1 >> s1 >> s1;
	// on lit les lignes "j N N"
	for (int i = 0; i < nbJ; i++) {
		int indexPart, counted;
		ifs >> s1 >> indexPart >> counted;
		if (counted) {
			pizza.put(possibleParts[indexPart]);
		}
	}
	ifs.close();
	cerr << "Linear solving: slice added to pizza" << endl;
	
	
	if (pizza.numberFilled >= bestPizza->numberFilled) {
		cerr << "Nouveau score : " << pizza.numberFilled << endl;
		pizza.outputToFile();
		*bestPizza = pizza;
	}
	cerr << "Linear solving: end" << endl;
	
}






string babFileName(int iGlobal) {
	stringstream ss; ss << iGlobal;
	return "bab"+ss.str()+".tmp";
}

void write_uint32_t(ostream& ofs, uint32_t value) {
	ofs.write((char*)&value, sizeof(uint32_t));
}
void write_vectorOfuint32_t(ostream& ofs, vector<uint32_t>& values) {
	ofs.write((char*)&(values[0]), values.size() * sizeof(uint32_t));
}

uint32_t read_uint32_t(istream& ifs) {
	uint32_t value;
	ifs.read((char*)&value, sizeof(uint32_t));
	return value;
}

void branchAndBoundFill(Pizza& pizza, vector<PartRoyale>& possibleParts) {
	
	struct Combinaison{
		vector<uint32_t> indexParts; uint32_t score;
		
		void writeToFile(ostream &ofs) {
			write_uint32_t(ofs, score); // S
			write_uint32_t(ofs, indexParts.size()); // Nn
			write_vectorOfuint32_t(ofs, indexParts); // I
		}
		
		void fillWithInput(istream &ifs) {
			score = read_uint32_t(ifs);
			indexParts.clear();
			uint32_t size = read_uint32_t(ifs);
			for (int i = 0; i < size; i++) {
				indexParts.push_back(read_uint32_t(ifs));
			}
		}
		
		// toutes les comparaisons sont inversés !!!!!
		// pour la fonction de tri
		bool operator==(const Combinaison& o) const { return score == o.score; };
		bool operator<(const Combinaison& o) const { return score > o.score; };
		bool operator>(const Combinaison& o) const { return score < o.score; };
		bool operator<=(const Combinaison& o) const { return score >= o.score; };
		bool operator>=(const Combinaison& o) const { return score <= o.score; };
		bool operator!=(const Combinaison& o) const { return score != o.score; };
		// attention valeur de retour inversés
		// -------------------------------------------
	};
	
	
	/*
		Format des fichiers babX.tmp
		X = le numéro d'itération principale
		en binaire
		tous les entiers en uint32_t
		
		pour chaque part pour lequel on stocke au moins une combinaison
			P			index de la part
			N			nombre de combinaison à lire
			pour chaque combinaison
				S		score de la combinaison
				Nn		nombre de part dans la combinaison
				pour chaque part
					I	son index
		
	*/
	
	
	// max 3672 octets / combinaison
	// max  918  parts / combinaison
	uint64_t nBase = 100;
	// 300000 combinaisons = environ 1 Go RAM
	unsigned int n; // 500
	// prépare la toute première itération
	ogzstream ofs(babFileName(0).c_str(), ios::out | ios::binary);
	write_uint32_t(ofs, 0); // P
	write_uint32_t(ofs, 1); // N
	Combinaison().writeToFile(ofs);
	ofs.close();
	
	
	for (int iGlobal = 0; ; iGlobal++) {
		// fichier d'entrée pour l'itération courante
		igzstream ifs(babFileName(iGlobal).c_str(), ios::in | ios::binary);
		// fichier de sortie de l'itération courante
		ogzstream ofsNext(babFileName(iGlobal+1).c_str(), ios::out | ios::binary);
		vector<Combinaison> cmbPossibles;
		int32_t nextPartInFile = read_uint32_t(ifs);
		cerr << ifs.tellg() << endl;
		if (!ifs.good()) {
			break;
		}
		bool nextPartInFileWaiting = true;
		
		for (uint32_t iPart = nextPartInFile; iPart < possibleParts.size(); iPart++) {
			PartRoyale p = possibleParts[iPart];
			// score minimum d'une combinaison pour la part
			int minCmbScore = max(0.f, pizza.width * (p.getCenterY() - (pizza.maxRoyale / 2)) - 500);
			
			int nbCombiStart = cmbPossibles.size();
			
			double nMult = possibleParts.size() / (double)(iPart + 1);
			
			n = nBase * nMult;
			
			uint32_t nbCombiToAdd = 0;
			// récupération des combinaisons depuis le fichier
			if (nextPartInFileWaiting && nextPartInFile == iPart) {
				nbCombiToAdd = read_uint32_t(ifs);
				for (int iCmbFile = 0; iCmbFile < nbCombiToAdd; iCmbFile++) {
					Combinaison c;
					c.fillWithInput(ifs);
					cmbPossibles.push_back(c);
				}
				if (ifs.good()) {
					nextPartInFile = read_uint32_t(ifs);
					nextPartInFileWaiting = ifs.good();
				}
				else {
					ifs.close();
					nextPartInFileWaiting = false;
				}
			}
			if (cmbPossibles.size() == 0 && iGlobal > 0 && nextPartInFileWaiting && nextPartInFile > iPart) {
				cerr << "It=" << iGlobal
					<< " Sl=" << iPart
					<< " No combination for this slice. Jumping to slice " << nextPartInFile
					<< endl;
				iPart = nextPartInFile-1; // sera réincrémenté à l'itération suivante (instruction boucle for)
				continue;
			}
			if (cmbPossibles.size() == 0 && (iGlobal == 0 || !nextPartInFileWaiting || nextPartInFile <= iPart)) {
				cerr << "It=" << iGlobal
					<< " Sl=" << iPart
					<< " Finished prematurely. No combination available for current slice."
					<< endl;
				break;
			}
			int nbIntermediateCmb = cmbPossibles.size();
			
			// on parcours tous les cas possibles actuels (mais pas les nouvelles qu'on ajoute au fur et à mesure)
			for (int iCmb = 0; iCmb < nbIntermediateCmb; iCmb++) {
				Combinaison c = cmbPossibles[iCmb];
				// on vérifie si la part courante peut être ajoutée à la combinaison actuelle sans
				// entrer en collision avec aucune part
				bool collide = false;
				for (int iPartCmb = c.indexParts.size() - 1; !collide && iPartCmb >= 0; iPartCmb--) {
					PartRoyale pCmb = (*pizza.possibleParts)[c.indexParts[iPartCmb]];
					collide = p.collideWith(pCmb);
				}
				if (!collide) {
					Combinaison c2 = c;
					c2.indexParts.push_back(p.index);
					c2.score += p.getArea();
					cmbPossibles.push_back(c2);
				}
			}
			sort(cmbPossibles.begin(), cmbPossibles.end());
			uint32_t newNbCombine = cmbPossibles.size();
			// on filtre les combinaisons à un score trop faible (par rapport à la part actuelle)
			while (cmbPossibles.size() > 0 && cmbPossibles[cmbPossibles.size()-1].score < minCmbScore) {
				cmbPossibles.pop_back();
			}
			
			uint32_t newNbAfterRemoveUseless = cmbPossibles.size();
			uint32_t nbPartToRemove = 0;
			if (cmbPossibles.size() > n) {
				// sauvegarder dans le fichier
				write_uint32_t(ofsNext, iPart+1);
				nbPartToRemove = cmbPossibles.size() - n;
				write_uint32_t(ofsNext, nbPartToRemove);
				for (int iCmb = n; iCmb < cmbPossibles.size(); iCmb++) {
					cmbPossibles[iCmb].writeToFile(ofsNext);
				}
				cmbPossibles.resize(n);
			}
			
			
			cerr << "It=" << iGlobal
				<< " Sl=" << iPart << "/" << possibleParts.size()
				<< " Cmb(Start=" << nbCombiStart
					<< " FromFile=" << nbCombiToAdd
					<< " Gen=" << (newNbCombine-nbIntermediateCmb)
					<< " RemUnderMin=" << (newNbCombine-newNbAfterRemoveUseless)
					<< " Total=" << newNbAfterRemoveUseless
					<< " Max=" << n
					<< " ToFile=" << nbPartToRemove
				<< ") MinCmb=" << minCmbScore
				<< " WorstCmb=" << ((cmbPossibles.size() > 0) ? cmbPossibles[cmbPossibles.size() - 1].score : 0)
				<< " BestCmb=" << ((cmbPossibles.size() > 0) ? cmbPossibles[0].score : 0)
				<< " BestScore=" << (*bestPizza).numberFilled
				<< endl;
			
			if (cmbPossibles[0].score > bestPizza->numberFilled) {
				// appliquer la meilleure combi sur la pizza
				for (int iCmb = 0; iCmb < cmbPossibles[0].indexParts.size(); iCmb++) {
					PartRoyale pCmb = (*pizza.possibleParts)[cmbPossibles[0].indexParts[iCmb]];
					pizza.put(pCmb);
				}
				cerr << "Nouveau score : " << pizza.numberFilled << endl;
				pizza.outputToFile();
				*bestPizza = pizza;
			}
		}
		ofsNext.close();
		ifs.close();
		system((string("rm ")+babFileName(iGlobal)).c_str());
	}
}









void fillParts(Pizza& pizza, int xMin, int xMax, int yMin, int yMax) {
	
	cerr << "Parts possibles sur la pizza : " << pizza.possibleParts->size() << endl; 
	
	long long count = 0;
	
	
	for (int line=0; line<pizza.height; line++) {
		
		vector<PartRoyale> possibleParts;
		for (int i = 0; i < (*(pizza.possibleParts)).size(); i++) {
			PartRoyale p = (*(pizza.possibleParts))[i];
			if (p.yMax == line && p.yMin == p.yMax && pizza.canPut(p, false)) {
				possibleParts.push_back(p);
			}
		}
		
		if (possibleParts.size() == 0)
			continue;
		
		cerr << "Ligne " << line << " : parts possibles " << possibleParts.size() << endl;
		
		int oldScore = pizza.numberFilled;
		
		
		linearFill(pizza, possibleParts);
		pizza = *bestPizza;
		cerr << "Lignes " << line
			<< " : points gagnés : " << (pizza.numberFilled - oldScore)
			<< " - Nouveau score : " << pizza.numberFilled << endl;
		
	}
	
	
	
	int MIN_SIZE = 10;
	int MAX_SIZE = 20;
	
	
	cerr << "Score courant : " << pizza.numberFilled << endl;
	
	// on prends en compte les paramètres [xy]M(in|ax)
	if (!pizza.isChunkFull(xMin, xMax, yMin, yMax)) {
		cerr << "Prise en compte des arguments xMin, xMax, yMin, yMax" << endl;
		pizza.cleanChunk(true, xMin, xMax, yMin, yMax);
	}
	
	while(1) {
		// on essaye de positionner le plus de parts possibles dans les espaces libres
		vector<PartRoyale> actualPossibleParts;
		for (vector<PartRoyale>::iterator it = pizza.possibleParts->begin(); it != pizza.possibleParts->end(); ++it) {
			if (pizza.canPut(*it, false)) {
				actualPossibleParts.push_back(*it);
			}
		}
		
		
		if (actualPossibleParts.size() > 0) {
			cerr << "Parts possibles : " << actualPossibleParts.size() << endl;
			linearFill(pizza, actualPossibleParts);
		}
		
		pizza = *bestPizza;
		
		// pizza.put(possibleParts[rand() % possibleParts.size()]);
		// remplacé par :
		do {
			xMin = rand() % (pizza.width - MIN_SIZE);
			xMax = (rand() % min((pizza.width - MIN_SIZE) - xMin, MAX_SIZE)) + xMin + MIN_SIZE;
			yMin = rand() % (pizza.height - MIN_SIZE);
			yMax = (rand() % min((pizza.height - MIN_SIZE) - yMin, MAX_SIZE)) + yMin + MIN_SIZE;
		} while(pizza.isChunkFull(xMin, xMax, yMin, yMax));
		pizza.cleanChunk(true, xMin, xMax, yMin, yMax);
		
	}
	
	
}















int main(int argc, char** argv) {
	
	srand(time(NULL));
	
	ifstream bestScoreFile("best.txt", ifstream::in);
	bestScoreFile >> previousExecBest;
	bestScoreFile.close();
	
	Pizza pizza(cin, PartRoyale::compareByCenterPosition);
	
	cerr << "Nombre de jambon : " << pizza.numberHam << endl;
	
	stringstream ss; ss << previousExecBest;
	ifstream bestPizzaFile("result"+ss.str()+".out", ifstream::in);
	pizza.fillWithInput(bestPizzaFile);
	bestPizzaFile.close();
	
	bestPizza = new Pizza(pizza);
	
	if (argc > 1 && strcmp(argv[1], "print") == 0) {
		pizza.displayPizza(cout);
		
		ofstream ofi("print_image.ppm", ofstream::out);
		pizza.displayPPM(ofi);
		ofi.close();
		return 0;
	}
	
	int xMin = 0, xMax = 0, yMin = 0, yMax = 0;
	if (argc > 4) {
		xMin = atoi(argv[1]);
		xMax = atoi(argv[2]);
		yMin = atoi(argv[3]);
		yMax = atoi(argv[4]);
		cerr << "xMin=" << xMin
			<< " xMax=" << xMax
			<< " yMin=" << yMin
			<< " yMax=" << yMax << endl;
	}
	
	// fillParts(pizza, xMin, xMax, yMin, yMax); // ça ne fini jamais
	
	branchAndBoundFill(pizza, (*pizza.possibleParts));
	
	
	
	
	
	
}


