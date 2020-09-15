package project2

import project1.Sample

object Sample2 {
  def sample(): Int = Sample.sample() + 1
  def sample1(): Int = 2

  def main(args: Array[String]) = {
    println("Hello, world")
  }
}
