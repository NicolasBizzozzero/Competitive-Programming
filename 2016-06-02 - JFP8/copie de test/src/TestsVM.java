/**
 * Created by twodn-1 on 02/06/16.
 */
public class TestsVM {
    public Tortue testTortue()
    {
        Terrain terrain = new Terrain(10, 10);
        Tortue tortue = new Tortue(terrain);
        return tortue;
    }

    public void testVM0()
    {
        String code[] = {""};
        VM vm = new VM(code,testTortue());
        System.out.println(vm.exec());
    }

    public void testVM1()
    {
        String code[] = {"move", "test 0"};
        VM vm = new VM(code,testTortue());
        System.out.println(vm.exec());
    }
}
