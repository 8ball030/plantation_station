set -e 

# fetch the agent from the local package registry
aea fetch zarathustra/plantation --local

# go to the new agent
cd plantation

# install the agent Note this causes a dependency issue
echo "Skilling install of aea deps" 
# aea install

# create and add a new ethereum key
aea generate-key ethereum && aea add-key ethereum

# install any agent deps
aea install

# issue certificates for agent to agent communications
aea issue-certificates

# finally, run the agent
aea run
