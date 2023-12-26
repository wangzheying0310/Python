function main(workbook) {
    let selectedSheet = workbook.getActiveWorksheet();
    var file_name =  workbook.getName()

    if (file_name.includes('Q=min'))
      var symbo = -1
    else
      if(file_name.includes('Q=max'))
        var symbo = 1
      else
        var symbo = 0
    var file_str = file_name.split("@", 2)
    //----------------------参数---------------------------//
    var Pn = 6000                        //机型额定功率
    var Q_ratio = (Math.random() * 0.1 + 48.43 + Number(file_str[0].slice(-2))*0.009)/100           //无功系数(百分比)
    var P_ratio = 4800.0 / 3840.0;            //有功系数
    var update = 200;                   //刷新率
    var Vbattery = 48.12;              //电池电压//程序232行：指定电压时修改有效，原数据修改无效
    var phase_1 = false;                //强制单相数据 ！慎用
    var phase_3 = false;                //强制三相数据 ！慎用


    //----------------------------------------------------//

    var phase = 0

    let header_3phase = [["Store No.", "Date", "Time", "Millisecond", "Urms-1-Total", "Urms-2-Total", "Urms-3-Total", "Irms-1-Total", "Irms-2-Total", "Irms-3-Total", "FreqU-1-Total", "P-SigmaA-Total", "S-SigmaA-Total", "Q-SigmaA-Total", "PF-SigmaA-Total", "Urms-4-Total", "Irms-4-Total", "P-4-Total"]]
    let header_1phase = [["Store No.", "Date", "Time", "Millisecond", "Urms-4-Total", "Irms-4-Total", "FreqU-4-Total", "P-4-Total", "S-4-Total", "Q-4-Total", "PF-4-Total", "Urms-1-Total", "Irms-1-Total","P-1-Total"]]



    let header = selectedSheet.getRange("A22").getExtendedRange(ExcelScript.KeyboardDirection.right).getValues()

    if (header[0].length == header_3phase[0].length || header[0].length == header_1phase[0].length) {
        for (let i = 0; i < header[0].length; i++) {
            if (header[0][i] == header_1phase[0][i]) {
                phase = 1
            }
            else {
                if (header[0][i] == header_3phase[0][i]) {
                    phase = 3
                }
                else {
                    phase = 0
                }
            }
        }
    }
    else {
        console.log("数据不匹配！")

    }
    if (update == 1000) {
        selectedSheet.getRange("D23").setFormulaLocal("=round(randbetween(55,955),0)");
        selectedSheet.getRange("D24").setFormulaLocal("=round($D$23+randbetween(-5,5),0)");
        selectedSheet.getRange("D24").autoFill();
    }

    if (phase == 1 || phase_1) {

        // 日期修改-根据首行
        selectedSheet.getRange("B24").setFormulaLocal("=B23");
        selectedSheet.getRange("B24").autoFill();
        // 时间修改-根据首行
        selectedSheet.getRange("C24").setFormulaLocal("=C23+1/24/60/60/" + String(1000 / update));
        selectedSheet.getRange("C24").autoFill();

        //电压微调-随机数
        var num_1 = 0.01 * Math.round(Math.random() * 11)
        var num_2 = -0.01 * Math.round(Math.random() * 11)
        var voltage_num = num_1 + num_2
        selectedSheet.getRange("E:E").insert(ExcelScript.InsertShiftDirection.right);
        selectedSheet.getRange("E23").setFormulaLocal("=round(F23+" + String(voltage_num) + "+randbetween(-10,10)*0.01,2)");
        selectedSheet.getRange("E23").autoFill();
        selectedSheet.getRange("F23").copyFrom(selectedSheet.getRange("E23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false);
        selectedSheet.getRange("E:E").delete(ExcelScript.DeleteShiftDirection.left);

        //功率微调-*P_ratio
        var num_3 = 1.0 * Math.round(Math.random() * 3)
        var num_4 = -1.0 * Math.round(Math.random() * 3)
        var p_in_num = num_3 + num_4

        selectedSheet.getRange("H:H").insert(ExcelScript.InsertShiftDirection.right);
        selectedSheet.getRange("H23").setFormulaLocal("=round(I23*" + String(P_ratio) + "+" + String(p_in_num) + ",0)");
        selectedSheet.getRange("H23").autoFill();
        selectedSheet.getRange("I23").copyFrom(selectedSheet.getRange("H23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false);
        selectedSheet.getRange("H:H").delete(ExcelScript.DeleteShiftDirection.left);

        // //P-in 跟随P同步修改

        selectedSheet.getRange("N:N").insert(ExcelScript.InsertShiftDirection.right);
        selectedSheet.getRange("N23").setFormulaLocal("=round(O23*" + String(P_ratio) + "+" + String(p_in_num) + ",0)");
        selectedSheet.getRange("N23").autoFill();
        selectedSheet.getRange("O23").copyFrom(selectedSheet.getRange("N23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false);
        selectedSheet.getRange("N:N").delete(ExcelScript.DeleteShiftDirection.left);

        //U -in 微调
        var num_5 = 0.01 * Math.round(Math.random() * 1)
        var num_6 = -0.01 * Math.round(Math.random() * 1)
        var voltage_in = num_5 + num_6
        selectedSheet.getRange("L:L").insert(ExcelScript.InsertShiftDirection.right);
        selectedSheet.getRange("L23").setFormulaLocal("=round(M23+" + String(voltage_in) + "+randbetween(-10,10)*0.001,2)");
        selectedSheet.getRange("L23").autoFill();
        selectedSheet.getRange("M23").copyFrom(selectedSheet.getRange("L23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false);
        selectedSheet.getRange("L:L").delete(ExcelScript.DeleteShiftDirection.left);



        //I-in计算
        selectedSheet.getRange("M23").setFormulaLocal("=round(abs(N23/L23),3)");
        selectedSheet.getRange("M23").autoFill();


        //功率去0-随机数
        selectedSheet.getRange("H:H").insert(ExcelScript.InsertShiftDirection.right);
        selectedSheet.getRange("H23").setFormulaLocal("=round(if(I23=0,randbetween(1,9),I23),0)");
        selectedSheet.getRange("H23").autoFill();
        selectedSheet.getRange("I23").copyFrom(selectedSheet.getRange("H23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false);
        selectedSheet.getRange("H:H").delete(ExcelScript.DeleteShiftDirection.left);

        //无功-Pn*Q_ratio

        selectedSheet.getRange("J:J").insert(ExcelScript.InsertShiftDirection.right);
        if (symbo !=0)
        {
        selectedSheet.getRange("J23").setFormulaLocal("=round("+String(Pn) +"*"+ String(Q_ratio) +"*"+String(symbo)+"+randbetween(-8,9),0)")
        }
        else{
          selectedSheet.getRange("J23").setFormulaLocal("=round(K23+" + "randbetween(-8,9),0)")
        }
        selectedSheet.getRange("J23").autoFill();
        selectedSheet.getRange("K23").copyFrom(selectedSheet.getRange("J23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false);
        selectedSheet.getRange("J:J").delete(ExcelScript.DeleteShiftDirection.left);

        //无功去0-随机数
        selectedSheet.getRange("J:J").insert(ExcelScript.InsertShiftDirection.right);
        selectedSheet.getRange("J23").setFormulaLocal("=round(if(K23=0,randbetween(1,9),K23),0)");
        selectedSheet.getRange("J23").autoFill();
        selectedSheet.getRange("K23").copyFrom(selectedSheet.getRange("J23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false);
        selectedSheet.getRange("J:J").delete(ExcelScript.DeleteShiftDirection.left);

        //视在功率-PQ计算
        selectedSheet.getRange("I23").setFormulaLocal("=round(sqrt(H23^2+J23^2),0)");
        selectedSheet.getRange("I23").autoFill();

        //功率因数-PS计算
        selectedSheet.getRange("K23").setFormulaLocal("=round(H23/I23,4)");
        selectedSheet.getRange("K23").autoFill();

        //电流-SU计算
        selectedSheet.getRange("F23").setFormulaLocal("=round(I23/E23,3)");
        selectedSheet.getRange("F23").autoFill();
        //PSQ格式
        let columns_H23 = selectedSheet.getRange("H23:J23");
        let columns_format_H23 = columns_H23.getExtendedRange(ExcelScript.KeyboardDirection.down);
        columns_format_H23.setNumberFormat("0.00000E+00");
        //P-in格式
        let columns_N23 = selectedSheet.getRange("N23");
        let columns_format_N23 = columns_N23.getExtendedRange(ExcelScript.KeyboardDirection.down);
        columns_format_N23.setNumberFormat("0.00000E+00");


    }

    if (phase == 3 || phase_3) {

      // 日期修改-根据首行
      selectedSheet.getRange("B24").setFormulaLocal("=B23");
      selectedSheet.getRange("B24").autoFill();
      // 时间修改-根据首行
      selectedSheet.getRange("C24").setFormulaLocal("=C23+1/24/60/60/" + String(1000 / update));
      selectedSheet.getRange("C24").autoFill();

        //电压微调-随机数
        var num_1 = 0.01 * Math.round(Math.random() * 11)
        var num_2 = -0.01 * Math.round(Math.random() * 11)
        var num_1_1 = 0.01 * Math.round(Math.random() * 11)
        var num_2_1 = -0.01 * Math.round(Math.random() * 11)
        var num_1_2 = 0.01 * Math.round(Math.random() * 11)
        var num_2_2 = -0.01 * Math.round(Math.random() * 11)

        var random_num_1 = num_1 + num_2
        var random_num_2 = num_1_1 + num_2_1
        var random_num_3 = num_1_2 + num_2_2


        //电压微调-随机数
        selectedSheet.getRange("E:E").insert(ExcelScript.InsertShiftDirection.right)
        selectedSheet.getRange("E23").setFormulaLocal("=round(F23+" + String(random_num_1) + "+randbetween(-10,10)*0.01,2)")
        selectedSheet.getRange("E23").autoFill()
        selectedSheet.getRange("F23").copyFrom(selectedSheet.getRange("E23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false)
        selectedSheet.getRange("E:E").delete(ExcelScript.DeleteShiftDirection.left)

        selectedSheet.getRange("F:F").insert(ExcelScript.InsertShiftDirection.right)
        selectedSheet.getRange("F23").setFormulaLocal("=round(G23+" + String(random_num_2) + "+randbetween(-10,10)*0.01,2)")
        selectedSheet.getRange("F23").autoFill()
        selectedSheet.getRange("G23").copyFrom(selectedSheet.getRange("F23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false)
        selectedSheet.getRange("F:F").delete(ExcelScript.DeleteShiftDirection.left)

        selectedSheet.getRange("G:G").insert(ExcelScript.InsertShiftDirection.right)
        selectedSheet.getRange("G23").setFormulaLocal("=round(H23+" + String(random_num_3) + "+randbetween(-10,10)*0.01,2)")
        selectedSheet.getRange("G23").autoFill()
        selectedSheet.getRange("H23").copyFrom(selectedSheet.getRange("G23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false)
        selectedSheet.getRange("G:G").delete(ExcelScript.DeleteShiftDirection.left)

        //功率*Ratio
        selectedSheet.getRange("L:L").insert(ExcelScript.InsertShiftDirection.right)
        selectedSheet.getRange("L23").setFormulaLocal("=round(M23*" + String(P_ratio) + "+randbetween(-3,3),0)")
        selectedSheet.getRange("L23").autoFill()
        selectedSheet.getRange("M23").copyFrom(selectedSheet.getRange("L23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false)
        selectedSheet.getRange("L:L").delete(ExcelScript.DeleteShiftDirection.left)

        //功率去0-随机数
        selectedSheet.getRange("L:L").insert(ExcelScript.InsertShiftDirection.right)
        selectedSheet.getRange("L23").setFormulaLocal("=round(if(M23=0,randbetween(1,9),M23),0)")
        selectedSheet.getRange("L23").autoFill()
        selectedSheet.getRange("M23").copyFrom(selectedSheet.getRange("L23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false)
        selectedSheet.getRange("L:L").delete(ExcelScript.DeleteShiftDirection.left)

      //========================== //P-in 跟随P同步修改-------实验
      var num_33 = 1.0 * Math.round(Math.random() * 3)
      var num_34 = -1.0 * Math.round(Math.random() * 3)
      var p3_in_num = num_33 + num_34

      selectedSheet.getRange("R:R").insert(ExcelScript.InsertShiftDirection.right);
      selectedSheet.getRange("R23").setFormulaLocal("=round(S23*" + String(P_ratio) + "+" + String(p3_in_num) + ",0)");
      selectedSheet.getRange("R23").autoFill();
      selectedSheet.getRange("S23").copyFrom(selectedSheet.getRange("R23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false);
      selectedSheet.getRange("R:R").delete(ExcelScript.DeleteShiftDirection.left);


      // ************************以下2选一****************************************************************************

      //1**************U -in 微调[原电池电压修改]
      // var num_35 = 0.01 * Math.round(Math.random() * 1)
      // var num_36 = -0.01 * Math.round(Math.random() * 1)
      // var voltage3_in = num_35 + num_36
      // selectedSheet.getRange("P:P").insert(ExcelScript.InsertShiftDirection.right);
      // selectedSheet.getRange("P23").setFormulaLocal("=round(Q23+" + String(voltage3_in) + "+randbetween(-10,10)*0.001,2)");
      // selectedSheet.getRange("P23").autoFill();
      // selectedSheet.getRange("Q23").copyFrom(selectedSheet.getRange("P23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false);
      // selectedSheet.getRange("P:P").delete(ExcelScript.DeleteShiftDirection.left);

      //2**************U -in 微调[指定电池电压修改]
      var num_35 = 0.01 * Math.round(Math.random() * 1)
      var num_36 = -0.01 * Math.round(Math.random() * 1)
      var voltage3_in = num_35 + num_36
      var P23=selectedSheet.getRange("P23")
      P23.setFormulaLocal("=round(" + String(Vbattery+voltage3_in) + "+randbetween(-10,10)*0.001,2)")
      P23.autoFill();


      //I-in计算
      selectedSheet.getRange("Q23").setFormulaLocal("=round(abs(R23/P23),3)");
      selectedSheet.getRange("Q23").autoFill();

      //=================================

        //无功-Q*Q_ratio
        selectedSheet.getRange("N:N").insert(ExcelScript.InsertShiftDirection.right);

        if (symbo != 0) {
          selectedSheet.getRange("N23").setFormulaLocal("=round(" + String(Pn) + "*" + String(Q_ratio) + "*" + String(symbo) + "+randbetween(-10,10),0)")
        }
        else {
          selectedSheet.getRange("N23").setFormulaLocal("=round(O23+" + "randbetween(-10,10),0)")
        }


        selectedSheet.getRange("N23").autoFill();
        selectedSheet.getRange("O23").copyFrom(selectedSheet.getRange("N23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false);
        selectedSheet.getRange("N:N").delete(ExcelScript.DeleteShiftDirection.left);

        //无功去0-随机数
        selectedSheet.getRange("N:N").insert(ExcelScript.InsertShiftDirection.right)
        selectedSheet.getRange("N23").setFormulaLocal("=round(if(O23=0,randbetween(1,9),O23),0)")
        selectedSheet.getRange("N23").autoFill()
        selectedSheet.getRange("O23").copyFrom(selectedSheet.getRange("N23").getExtendedRange(ExcelScript.KeyboardDirection.down), ExcelScript.RangeCopyType.values, false, false)
        selectedSheet.getRange("N:N").delete(ExcelScript.DeleteShiftDirection.left)

        //视在功率-sqrt(P^2+Q^2)计算
        selectedSheet.getRange("M23").setFormulaLocal("=round(sqrt(L23^2+N23^2),0)")
        selectedSheet.getRange("M23").autoFill()

        //功率因数-P/S计算
        selectedSheet.getRange("O23").setFormulaLocal("=round(L23/M23,4)");
        selectedSheet.getRange("O23").autoFill();

        //电流1-S/3/U计算
        selectedSheet.getRange("H23").setFormulaLocal("=round(M23/3/E23,3)")
        selectedSheet.getRange("H23").autoFill()

        selectedSheet.getRange("J23").setFormulaLocal("=round(M23/3/G23,3)")
        selectedSheet.getRange("J23").autoFill()

        selectedSheet.getRange("I23").setFormulaLocal("=round((M23-E23*H23-G23*J23)/F23,3)")
        selectedSheet.getRange("I23").autoFill()

        let columns_H23 = selectedSheet.getRange("L23:N23")
        let columns_format_H23 = columns_H23.getExtendedRange(ExcelScript.KeyboardDirection.down)
        columns_format_H23.setNumberFormat("0.00000E+00")

    }

  }