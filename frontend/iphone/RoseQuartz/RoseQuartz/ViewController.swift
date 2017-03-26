//
//  ViewController.swift
//  RoseQuartz
//
//  Created by Tamby Kaghdo on 3/19/17.
//  Copyright © 2017 Tamby Kaghdo. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    //MARK: Properties
    
    @IBOutlet weak var nameTextField: UITextField!
    @IBOutlet weak var emailTextField: UITextField!
    @IBOutlet weak var pwTextField: UITextField!
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    // MARK: helper methods
    
    func exec_post_request(){
        let dict = ["email": "test@gmail.com", "password":"123456", "name": "yy"] as [String: Any]
        if let jsonData = try? JSONSerialization.data(withJSONObject: dict, options: []) {
            
            
            let url = NSURL(string: "http://localhost:8000/signup")!
            let request = NSMutableURLRequest(url: url as URL)
            request.httpMethod = "POST"
            
            request.httpBody = jsonData
            
            let task = URLSession.shared.dataTask(with: request as URLRequest){ data,response,error in
                
                do {
                    let json = try JSONSerialization.jsonObject(with: data!, options: .mutableContainers) as? NSDictionary
                    
                    if let parseJSON = json {
                        let resultValue:String = parseJSON["success"] as! String;
                        print("result: \(resultValue)")
                        print(parseJSON)
                    }
                } catch let error as NSError {
                    print(error)
                }
            }
            task.resume()
        }
    }
    
    func get_current_date() -> String {
        let currentDate = Date()
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyyMMdd"
        
        var str_curr_date: String
        str_curr_date = formatter.string(from: currentDate)
        
        return str_curr_date
    }
    
    //MARK: Actions
    
    
    @IBAction func signup(_ sender: UIButton) {
        
        //TODO: encode the values
        let userDict: [String:String] = [
            "name" : nameTextField.text!,
            "email" : emailTextField.text!,
            "password" : pwTextField.text!
        ]
        // create the user json
        do {
            let jsonData = try JSONSerialization.data(withJSONObject: userDict, options: .prettyPrinted)
            
            // write the the json to file
            let file = "signup_" + get_current_date() + ".json"
            
            if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
                //writing
                do {
                    let path = dir.appendingPathComponent(file)
                    try jsonData.write(to: path)
                    // send the json to backend
                    // exec_post_request()
                }
                catch {print(error)}
                defer{} //TODO: delete json file
            }
            
        }
        catch {
            print(error)
        }
        
        
        
        
        

    }
}

