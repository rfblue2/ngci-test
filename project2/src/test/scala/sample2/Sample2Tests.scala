package project2

import org.scalatest._
import org.scalatest.Matchers._

class Sample2Tests extends WordSpec with Matchers {

  "sample" should {
    "return 2" in {
      Sample2.sample() shouldBe 2
    }
  }
}
