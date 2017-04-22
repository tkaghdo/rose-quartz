//
//  LangSelectTableViewController.swift
//  RoseQuartz
//
//  Created by Tamby Kaghdo on 4/18/17.
//  Copyright © 2017 Tamby Kaghdo. All rights reserved.
//

import UIKit



class LangSelectTableViewController: UITableViewController {
    
    
    //var langData = [String]()
    var langData = ["A", "B", "C"]
    let index = 0
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false
        
        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // MARK: - Table view data source
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        return langData.count
    }
    
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "LangCell", for: indexPath)
        
        
        //cell.textLabel?.text = langData[indexPath.row]
        self.get_request{ jsonString in
            // and here you get the "returned" value from the asynchronous task
            cell.textLabel?.text = jsonString[indexPath.row]
        }
        
        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print("%%%")
        self.get_request{ jsonString in
            // and here you get the "returned" value from the asynchronous task
            print(jsonString[0])
        }
        performSegue(withIdentifier: "toQuestionsSegue", sender: langData[indexPath.row])
        
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if (segue.identifier == "toQuestionsSegue"){
            if let destination = segue.destination as? QuestionsViewController{
                destination.passedData = sender as? String
            }
        }
    }
    
    // MARK: helper methods
    
    func get_request(completion: @escaping ([String]) -> ()){
        let url = URL(string: "http://localhost:8000/languages")
        var json = [String]()
        let task = URLSession.shared.dataTask(with: url!) { data, response, error in
            guard error == nil else {
                print(error!)
                return
            }
            guard let data = data else {
                print("Data is empty")
                return
            }
            
            json = try! JSONSerialization.jsonObject(with: data, options: []) as! Array
            completion(json)
            
        }
        
        task.resume()
        
    }
    
    
    
}
