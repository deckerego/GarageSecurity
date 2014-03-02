package net.deckerego

import org.apache.camel.Exchange
import org.apache.camel.scala.dsl.builder.RouteBuilder

/**
 * A Camel Router using the Scala DSL
 */
class MyRouteBuilder extends RouteBuilder {

    // an example of a Processor method
   val myProcessorMethod = (exchange: Exchange) => {
     exchange.getIn.setBody("block test")
   }
   
   // a route using Scala blocks
   "timer://foo?period=5s" ==> {
      process(myProcessorMethod)
      to("log:block")
   }
}
