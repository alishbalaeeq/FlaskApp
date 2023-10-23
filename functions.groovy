def deploy(String branch_name) {
  if (branch_name == "production") {
    println "Deploying to Production."
  } else if (branch_name == "test") {
    println "Deploying to Test."
  } else {
    println "Deploying to Dev."
  }
}

def build() {
  echo 'Building'
  bat 'pip3 install -r requirements.txt'
}

def checkout() {
  git branch: 'main', url: 'https://github.com/alishbalaeeq/FlaskApp.git'
}

  return this
