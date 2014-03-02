package net.deckerego

import org.apache.camel.main.Main
import org.apache.camel.scala.dsl.builder.RouteBuilderSupport

/**
 * A Main to run Camel with MyRouteBuilder
 */
object MyRouteMain extends RouteBuilderSupport {

  def main(args: Array[String]) {
    val main = new Main()
    // enable hangup support so you need to use ctrl + c to stop the running app
    main.enableHangupSupport();
    main.addRouteBuilder(new MyRouteBuilder())
    // must use run to start the main application
    main.run();
  }
}

