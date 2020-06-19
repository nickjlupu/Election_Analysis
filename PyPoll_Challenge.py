# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate options list and candidate votes dictionary.
candidate_options = []
candidate_votes = {}
# create a list for the counties and dictionary to store votes cast in each county
county_list = []
county_votes = {}
# create an empty string that will hold the county name that had largest turnout
largest_turnout = ""
# declare a variable that represents the # of votes a county received
turnout_count = 0

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    
    # Loop thru rows in the CSV file to determine:
    # total votes
    # candidates & votes for
    # counties & voter turnout
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add to the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # Get the county name from each row.
        county_name = row[1]
        # If the county does not match any existing county, add to the county list
        if county_name not in county_list:
            # Add the county name to the county list.
            county_list.append(county_name)
            # And begin tracking that county's vote count.
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # County Votes header
    county_header = (
        f"\n"
        f"County Votes:\n")
    # Print the county header to the terminal.
    print(county_header, end="")
    # Save the county header to the text file.
    txt_file.write(county_header)

    # Loop thru county votes dictionary to determine votes by county & largest voter turnout
    for county in county_votes:
        # Retrieve county vote count and percentage.
        c_votes = county_votes[county]
        c_vote_percentage = float(c_votes) / float(total_votes) * 100
        county_results = (
                        f"{county}: {c_vote_percentage:.1f}% ({c_votes:,})\n")

        # Print each county's vote count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
        # Determine county with largest voter turnout.
        if (c_votes > turnout_count):
            turnout_count = c_votes
            largest_turnout = county
    
    # Print the largest county turnout to the terminal.
    turnout_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"-------------------------\n")
    print(turnout_summary)
    # Save the largest county turnout to the text file.
    txt_file.write(turnout_summary)
  
    # Loop thru candidate votes dictionary to determine votes for candidate & election winner
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


    






