import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Main {
	
	public static void main(String[] args) {
		
		Input in = new Input(System.in);
		
		
		/*
		for (String hyp1 : in.villes.keySet()) {
			for (String hyp2 : in.villes.keySet()) {
				if (hyp1.equals(hyp2))
					continue;
				int nbFasterInHyperloop = 0;
				
				for (Journey j : in.journeys) {
					String h1 = in.closestTo(j.ville1, hyp1, hyp2);
					String h2 = in.closestTo(j.ville2, hyp1, hyp2);
					
					double tHyperloop = in.timeHyperLoopSimple(h1, h2);

					double tStart = in.tempsVoiture(j.ville1, h1);
					double tEnd = in.tempsVoiture(j.ville2, h2);
					
					if (tHyperloop + tStart + tEnd < j.carTime) {
						nbFasterInHyperloop++;
					}
					
				}
				
				if (nbFasterInHyperloop >= in.n)
					System.out.println(hyp1 + " " + hyp2);
				
				
			}
		}*/
		
		
		/*
		
		Random r = new Random();
		List<String> villes = new ArrayList<>(in.villes.keySet());
		
		for (;;) {
			int nb = r.nextInt(30)+1;
			List<String> hyperloop = new ArrayList<>();
			for (int i = 0; i < nb; i++) {
				String h;
				while (hyperloop.contains(h = villes.get(r.nextInt(villes.size()))));
				hyperloop.add(h);
			}
		

			double hyperloopDist = 0;
			
			for (int i = 0; i < hyperloop.size() - 1; i++) {
				hyperloopDist += in.distance(hyperloop.get(i), hyperloop.get(i + 1));
			}
			
			
			if (hyperloopDist >= in.d) {
				continue;
			}
			
			
			int nbFasterInHyperloop = 0;
			
			for (Journey j : in.journeys) {
				
				String h1 = in.hyperloopClosestTo(j.ville1, hyperloop);
				String h2 = in.hyperloopClosestTo(j.ville2, hyperloop);

				int h1index = hyperloop.indexOf(h1);
				int h2index = hyperloop.indexOf(h2);

				int start = Math.min(h1index, h2index);
				int end = Math.max(h1index, h2index);
				
				double hyperloopTime = 0;
				
				for (int i = start; i < end; i++) {
					hyperloopTime += in.timeHyperLoopSimple(hyperloop.get(i), hyperloop.get(i + 1));
				}

				double timeStart = in.tempsVoiture(j.ville1, h1);
				double timeEnd = in.tempsVoiture(j.ville2, h2);
				
				if (hyperloopTime + timeEnd + timeStart < j.carTime)
					nbFasterInHyperloop++;
				
				
			}
			
			if (nbFasterInHyperloop >= in.n) {
				System.out.print(hyperloop.size());
				for (String h : hyperloop) {
					System.out.print(" " + h);
				}
				System.out.println();
				System.out.println("   nbfaster = " + nbFasterInHyperloop);

				
				System.out.println("   hyperloopDist = " + hyperloopDist);
			}
			
			
			
		}
		
		*/
		
		/*
		for (int nbStop = 2; nbStop <= 100; nbStop++) {
			
			List<String> hyperloop = new ArrayList<>();
			for (int i = 0; i < nbStop; i++) hyperloop.add(null);
			
			doLoop(nbStop, 0, in, hyperloop, () -> {
				
				
				
				
				int nbFasterInHyperloop = 0;
				
				for (Journey j : in.journeys) {
					
					String h1 = in.hyperloopClosestTo(j.ville1, hyperloop);
					String h2 = in.hyperloopClosestTo(j.ville2, hyperloop);

					int h1index = hyperloop.indexOf(h1);
					int h2index = hyperloop.indexOf(h2);

					int start = Math.min(h1index, h2index);
					int end = Math.max(h1index, h2index);
					
					double hyperloopTime = 0;
					
					for (int i = start; i < end; i++) {
						hyperloopTime += in.timeHyperLoopSimple(hyperloop.get(i), hyperloop.get(i + 1));
					}

					double timeStart = in.tempsVoiture(j.ville1, h1);
					double timeEnd = in.tempsVoiture(j.ville2, h2);
					
					if (hyperloopTime + timeEnd + timeStart < j.carTime)
						nbFasterInHyperloop++;
					
					
				}
				
				if (nbFasterInHyperloop >= in.n) {
					System.out.print(hyperloop.size());
					for (String h : hyperloop) {
						System.out.print(" " + h);
					}
					System.out.println();
					System.out.println("   nbfaster = " + nbFasterInHyperloop);

					double hyperloopDist = 0;
					
					for (int i = 0; i < hyperloop.size() - 1; i++) {
						hyperloopDist += in.distance(hyperloop.get(i), hyperloop.get(i + 1));
					}
					
					System.out.println("   hyperloopDist = " + hyperloopDist);
				}
				
				
				
			});
			
			
		}
		
		*/
		
		
		
		Random r = new Random();
		
		for (;;) {
			
			
			
			// génération des lignes
			List<String> villes = new ArrayList<>(in.villes.keySet());
			villes.remove(in.hub);
			
			
			List<List<String>> hyperloopLines = new ArrayList<>();
			
			int nbLines = r.nextInt(10) + 2;
			
			try {
				for (int i = 0; i < nbLines; i++) {
					List<String> hyperloop = new ArrayList<>();
					int nbArret = r.nextInt(20) + 2;
					for (int j = 0; j < nbArret; j++) {
						hyperloop.add(null);
					}
					
					hyperloop.set(r.nextInt(nbArret), in.hub);
					
					for (int j = 0; j < nbArret; j++) {
						if (hyperloop.get(j) != null)
							continue;
						String h;
						while (hyperloop.contains(h = villes.get(r.nextInt(villes.size()))));
						hyperloop.set(j, h);
						villes.remove(h);
					}
					
					hyperloopLines.add(hyperloop);
				}
			} catch(IllegalArgumentException e) {
				continue;
			}
			
			// vérification

			double hyperloopDist = 0;

			for (List<String> hyperloop : hyperloopLines) {
				for (int i = 0; i < hyperloop.size() - 1; i++) {
					hyperloopDist += in.distance(hyperloop.get(i), hyperloop.get(i + 1));
				}
			}
			
			
			if (hyperloopDist >= in.d) {
				continue;
			}
			
			
			
			
			
			int nbFasterInHyperloop = 0;
			
			
			for (Journey j : in.journeys) {
				
				if (hyperloopJourneyTime(in, j, hyperloopLines) < j.carTime) {
					nbFasterInHyperloop++;
				}
				
			}
			

			if (nbFasterInHyperloop >= in.n) {
				System.out.print(hyperloopLines.size());
				for (List<String> hyperloop : hyperloopLines) {
					System.out.print(" " + hyperloop.size());
					for (String h : hyperloop) {
						System.out.print(" " + h);
					}
				}
				System.out.println();
				System.out.println("   nbfaster = " + nbFasterInHyperloop);

				
				System.out.println("   hyperloopDist = " + hyperloopDist);
			}
			
			
			
			
			
		}
		
		
	}
	
	
	public static double hyperloopJourneyTime(Input in, Journey j, List<List<String>> hyperloopLines) {
		
		String h1 = in.hyperloopClosestToList(j.ville1, hyperloopLines);
		String h2 = in.hyperloopClosestToList(j.ville2, hyperloopLines);
		
		int indexLineH1 = -1, indexLineH2 = -1;
		
		for (int i = 0; i < hyperloopLines.size(); i++) {
			if (hyperloopLines.get(i).contains(h1) && hyperloopLines.get(i).contains(h2)) {
				indexLineH1 = indexLineH2 = i;
				break;
			}
			else if (hyperloopLines.get(i).contains(h1)) {
				indexLineH1 = i;
			}
			else if (hyperloopLines.get(i).contains(h2)) {
				indexLineH2 = i;
			}
		}
		
		
		double hyperloopTime = 0;
		
		if (indexLineH1 == indexLineH2) {
			
			List<String> hyperloop = hyperloopLines.get(indexLineH1);

			int h1index = hyperloop.indexOf(h1);
			int h2index = hyperloop.indexOf(h2);

			int start = Math.min(h1index, h2index);
			int end = Math.max(h1index, h2index);
			
			for (int i = start; i < end; i++) {
				hyperloopTime += in.timeHyperLoopSimple(hyperloop.get(i), hyperloop.get(i + 1));
			}
			
			
		}
		else {

			List<String> hyperloop = hyperloopLines.get(indexLineH1);

			int h1index = hyperloop.indexOf(h1);
			int h2index = hyperloop.indexOf(in.hub);

			int start = Math.min(h1index, h2index);
			int end = Math.max(h1index, h2index);
			
			for (int i = start; i < end; i++) {
				hyperloopTime += in.timeHyperLoopSimple(hyperloop.get(i), hyperloop.get(i + 1));
			}

			hyperloop = hyperloopLines.get(indexLineH2);

			h1index = hyperloop.indexOf(in.hub);
			h2index = hyperloop.indexOf(h2);

			start = Math.min(h1index, h2index);
			end = Math.max(h1index, h2index);
			
			for (int i = start; i < end; i++) {
				hyperloopTime += in.timeHyperLoopSimple(hyperloop.get(i), hyperloop.get(i + 1));
			}
			
			hyperloopTime += 300;
			
		}
		
		

		double timeStart = in.tempsVoiture(j.ville1, h1);
		double timeEnd = in.tempsVoiture(j.ville2, h2);
		
		return hyperloopTime + timeEnd + timeStart;
		
		
		
		
		
	}
	
	
	
	
	
	/*
	
	public static void doLoop(int deepTotal, int deepCurrent, Input in, List<String> hyperloop, Runnable r) {
		
		for (String ville : in.villes.keySet()) {
			
			if (hyperloop.contains(ville))
				continue;
			
			hyperloop.set(deepCurrent, ville);
			
			double hyperloopDist = 0;
			
			for (int i = 0; i < deepCurrent; i++) {
				hyperloopDist += in.distance(hyperloop.get(i), hyperloop.get(i + 1));
			}
			
			if (hyperloopDist >= in.d)
				continue;
			
			if (deepCurrent < deepTotal - 1) {
				doLoop(deepTotal, deepCurrent+1, in, hyperloop, r);
			}
			else
				r.run();
		}
		
		hyperloop.set(deepCurrent, null);
		
	}
	
	
	*/
	
	
	
	
	
}
