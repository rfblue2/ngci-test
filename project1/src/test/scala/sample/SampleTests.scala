package project1

import org.scalatest._
import org.scalatest.Matchers._

class SampleTests extends WordSpec with Matchers {

  "sample" should {
    "return 1" in {
      Sample.sample() shouldBe 1
    }
  }
}
