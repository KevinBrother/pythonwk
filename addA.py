#_*_coding:utf-8_*_
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = { 15, 25, 30, 35, 45, 50, 55, 70, 80, 100 };
            int sum = 150;
            foreach (var item in Solve(arr, sum))
            {
                Console.WriteLine(string.Join(", ", item.Skip(1)));
            }
        }
        static IEnumerable<IEnumerable<int>> Solve(int[] arr, int sum, IEnumerable<int> feed = null)
        {
            if (feed == null) feed = new List<int>() { 0 };
            if (feed.Sum() == sum) yield return feed;
            foreach (int n in arr.Where(x => x + feed.Sum() <= sum))
            {
                foreach (var item in Solve(arr, sum, feed.Concat(new int[] { n }))) yield return item;
            }
        }
    }
}