def deploy(String branch_name) {
  if (branch_name == "PROD") {
    println "Deploying to Production."
  } else if (branch_name == "TEST") {
    println "Deploying to Test."
  } else {
    println "Deploying to Dev."
  }
}

  return this
