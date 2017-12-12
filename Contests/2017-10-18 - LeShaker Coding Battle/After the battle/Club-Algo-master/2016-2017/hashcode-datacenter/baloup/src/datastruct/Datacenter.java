package datastruct;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

import javafx.util.Pair;

public class Datacenter {

	private static int bestScore = 0;
	private static Datacenter bestDatacenter;
	
	public static int getBestScore() {
		return bestScore;
	}
	public static void setBest(Datacenter ds) {
		int newScore = ds.getScore();
		if (newScore <= bestScore)
			return;
		
		bestDatacenter = new Datacenter(ds);
		bestScore = newScore;
		System.out.println("New runtime best score : "+bestScore);
	}
	
	
	
	private static int bestScoreFromFile = -1;
	static {

		try (Scanner s = new Scanner(new FileInputStream("best.dat"))) {
			bestScoreFromFile = s.nextInt();
		} catch (FileNotFoundException e) {
			
		}
	}
	
	
	
	
	
	
	
	
	
	
	

	private final LocState[][] matrixState;
	private final int[][] matrixServers;
	private final Server[] servers;
	public final int nbGroup;
	
	
	
	public Datacenter(InputStream in) {
		try(Scanner s = new Scanner(in)) {
	        int nbRangee = s.nextInt();
	        int nbPlace = s.nextInt();
	        int nbIndisp = s.nextInt();
	        nbGroup = s.nextInt();
	        int nbServers = s.nextInt();
	        
	        matrixState = new LocState[nbRangee][nbPlace];
	        for (int i=0; i<nbRangee; i++) {
	        	Arrays.fill(matrixState[i], LocState.EMPTY);
	        }
	        matrixServers = new int[nbRangee][nbPlace];
	        for (int i=0; i<nbRangee; i++) {
	        	Arrays.fill(matrixServers[i], -1);
	        }
	        
	        for (int i = 0; i < nbIndisp; i++) {
	            int rangee = s.nextInt(), empl = s.nextInt();
	            matrixState[rangee][empl] = LocState.UNAVAILABLE;
	        }
	        
	        servers = new Server[nbServers];
	        
	        for (int i = 0; i < nbServers; i++) {
	            int size = s.nextInt(), cap = s.nextInt();
	            servers[i] = new Server(size, cap, i);
			}
	        
	        
		}
		
	}
	
	public Datacenter(Datacenter in) {
		matrixState = Arrays.copyOf(in.matrixState, in.matrixState.length);
		for (int i = 0; i < matrixState.length; i++)
			matrixState[i] = Arrays.copyOf(matrixState[i], matrixState[i].length);
		
		servers = new Server[in.servers.length];
		Map<Server, Server> svOriginalToDest = new HashMap<>();
		for (int i = 0; i < servers.length; i++) {
			servers[i] = new Server(in.servers[i]);
			svOriginalToDest.put(in.servers[i], servers[i]);
		}
		
		
		matrixServers = Arrays.copyOf(in.matrixServers, in.matrixServers.length);
		for (int i = 0; i < matrixState.length; i++)
			matrixServers[i] = Arrays.copyOf(matrixServers[i], matrixServers[i].length);
		
		nbGroup = in.nbGroup;
	}
	
	
	
	
	public void restoreStateFromRuntimeBest() {
		if (bestScore <= getScore())
			return;
		for (int i = 0; i < matrixState.length; i++) {
			for (int j = 0; j < matrixState[i].length; j++) {
				matrixState[i][j] = bestDatacenter.matrixState[i][j];
				matrixServers[i][j] = bestDatacenter.matrixServers[i][j];
			}
		}
		
		for (int i = 0; i < servers.length; i++) {
			servers[i].row = bestDatacenter.servers[i].row;
			servers[i].col = bestDatacenter.servers[i].col;
			servers[i].group = bestDatacenter.servers[i].group;
		}
		
	}
	
	
	
	
	
	
	public void outputResult(PrintStream out) {
		for (Server sv : servers) {
			out.println(sv);
		}
	}
	
	public void outputToFile() throws FileNotFoundException {
		int newScore = getScore();
		if (newScore <= bestScoreFromFile)
			return;
		bestScoreFromFile = newScore;
		try (PrintStream ps = new PrintStream("result"+newScore+".out")) {
			outputResult(ps);
		}
		try (PrintStream ps = new PrintStream("best.dat")) {
			ps.print(newScore);
		}
		System.out.println("NEW GLOBAL BEST SCORE : "+newScore);
	}
	
	
	
	public void display(PrintStream out) {
		for (int r=0; r<matrixState.length; r++) {
			for (int c=0; c<matrixState[r].length; c++) {
				out.print(matrixState[r][c]);
			}
			out.println();
		}
	}
	
	
	public Server[] getServers() {
		return Arrays.copyOf(servers, servers.length);
	}
	
	
	public int getNbRow() {
		return matrixState.length;
	}
	
	public int getNbCol() {
		return matrixState[0].length;
	}
	
	
	
	

	public boolean canPut(Server s, int r, int c) {
		if (!canPutIgnoreOtherServers(s, r, c))
			return false;
		if (s.isPlaced())
			return false;
		for (int curC = c; curC < c+s.size; curC++)
			if (matrixState[r][curC] == LocState.FULL)
				return false;
		return true;
	}
	
	public boolean canPutIgnoreOtherServers(Server s, int r, int c) {
		if (s == null)
			return false;
		if (r < 0 || r >= getNbRow() || c < 0 || c > getNbCol()-s.size)
			return false;
		for (int curC = c; curC < c+s.size; curC++)
			if (matrixState[r][curC] == LocState.UNAVAILABLE)
				return false;
		return true;
	}
	
	public boolean put(Server s, int r, int c) {
		if (!canPutIgnoreOtherServers(s, r, c))
			return false;
		if (s.isPlaced())
			remove(s);

		for (int curC = c; curC < c+s.size; curC++) {
			if (matrixState[r][curC] == LocState.FULL) {
				remove(servers[matrixServers[r][curC]]);
			}
			matrixState[r][curC] = LocState.FULL;
			matrixServers[r][curC] = s.index;
		}

		s.row = r;
		s.col = c;
		return true;
	}
	
	public void remove(Server s) {
		if (s == null || !s.isPlaced())
			return;
		for (int curC = s.col; curC < s.col + s.size; curC++) {
			matrixState[s.row][curC] = LocState.EMPTY;
			matrixServers[s.row][curC] = -1;
		}
		s.row = -1;
		s.col = -1;
	}
	
	
	
	private Pair<Integer, Integer> computeScore() {
		int[][] scores = new int[getNbRow()][nbGroup];
		int[] maxScoreByGroups = new int[nbGroup];
		for (Server sv : servers) {
			if (!sv.isValid()) continue;
			scores[sv.row][sv.group] += sv.capacity;
			maxScoreByGroups[sv.group] += sv.capacity;
		}
		int min = Integer.MAX_VALUE;
		int minGroup = -1;
		for (int g=0; g<nbGroup; g++) {
			int maxRowScore = 0;
			for (int r=0; r<getNbRow(); r++) {
				maxRowScore = Math.max(scores[r][g], maxRowScore);
			}
			int minRow = maxScoreByGroups[g] - maxRowScore;
			if (minRow < min) {
				min = minRow;
				minGroup = g;
			}
		}
		
		return new Pair<>(min, minGroup);
	}
	
	public int getScore() {
		return computeScore().getKey();
	}
	
	public int getGroupWithMinScore() {
		return computeScore().getValue();
	}
	
	
	
	
	private enum LocState {
		EMPTY("."), FULL("#"), UNAVAILABLE("X");
		
		private String toString;
		
		private LocState(String toStr) {
			toString = toStr;
		}
		
		@Override
		public String toString() {
			return toString;
		}
	}
	
}
