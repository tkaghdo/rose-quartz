//
//  QuestionsViewController.swift
//  RoseQuartz
//
//  Created by Tamby Kaghdo on 4/18/17.
//  Copyright © 2017 Tamby Kaghdo. All rights reserved.
//

import UIKit

class QuestionsViewController: UIViewController {

    @IBOutlet weak var questionLabel: UILabel!
    var passedData: String!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        questionLabel.text = passedData
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
