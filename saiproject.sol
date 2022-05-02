pragma solidity ^0.4.21;
pragma experimental ABIEncoderV2;

/*
Election contract that allows the owner to issue voting rights
to anybody and also end the election and announce results
*/
contract Election {

    struct Candidate {
        string name;
        uint voteCount;
        string region;
    }

    struct Voter {
        bool authorized;
        bool voted;
        uint vote;
    }

    address public owner;
    string public electionName;

    mapping(address => Voter) public voters;
    Candidate[] public candidates;

    event ElectionResult(string candidateName, uint voteCount,string region);

    modifier ownerOnly() {
        require(msg.sender == owner);
        _;
    }

    function Election(string _name) public {
        owner = msg.sender;
        electionName = _name;
    }

    function addCandidate(string name,string region) ownerOnly public {
        candidates.push(Candidate(name, 0,region));
    }

    function authorize(address person) ownerOnly public {
        voters[person].authorized = true;
    }

    function vote(string _cname,string _region) public {
        //make sure voter is authorized and has not already voted
                
        require(!voters[msg.sender].voted);
        require(voters[msg.sender].authorized);
        uint  voteIndex=0;
                
        //get index
        for (uint i=0; i < candidates.length; i++){
                if(keccak256(bytes(candidates[i].region)) == keccak256(bytes(_region))){
                  if(keccak256(bytes(candidates[i].name)) == keccak256(bytes(_cname))){

                      voteIndex=i;
                  }}
         }
       
        voters[msg.sender].vote = voteIndex;
        voters[msg.sender].voted = true;

        //increase candidate vote count by 1
       
        candidates[voteIndex].voteCount += 1;
    }
    function get_candidates_region(string _cregion) view public returns (uint[]){
    uint []  rlist;
    var countt=0;
     for (uint i=0; i < candidates.length; i++){
                if(keccak256(bytes(candidates[i].region)) == keccak256(bytes(_cregion))){
                rlist.push(countt);
                countt=countt+1;
                }}
                return rlist;

    }
         
    function end() ownerOnly public {
        //announce each candidates results
        for(uint i=0; i < candidates.length; i++) {

            emit ElectionResult(candidates[i].name, candidates[i].voteCount,candidates[i].region);
        }

        //destroy the contract
        selfdestruct(owner);
    }
}
