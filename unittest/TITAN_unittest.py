import math as math
import titan
from titan import _general_charge_distribution_class as general
from titan import _charge_distribution_class_gen as gen
from titan import _quantification_txt as quant_txt
from titan import _input as input
import unittest

class TestGeneralChargeDistributionClass(unittest.TestCase):
    def test_oef_1_point_charge_bohr(self):
        charge_distribution = general.ChargeDistribution()
        charge_distribution.point_charge_list.append([[0.0, 0.0, 0.0], 1.0])
        self.assertEqual(charge_distribution.calculate_oriented_electric_field(1.0, 0.0, 0.0, 1.0, 0.0, 0.0, "BOHR"),
                         1.000)

    def test_oef_1_point_charge_ans(self):
        charge_distribution = general.ChargeDistribution()
        charge_distribution.point_charge_list.append([[0.0, 0.0, 0.0], 1.0])
        self.assertAlmostEqual(charge_distribution.calculate_oriented_electric_field(1.0, 0.0, 0.0, 1.0, 0.0, 0.0, "ANS"),
                    0.280, 3)

    def test_oef_2_point_charges(self):
        charge_distribution = general.ChargeDistribution()
        charge_distribution.point_charge_list.append([[0.0, 0.0, 0.0], 1.0])
        charge_distribution.point_charge_list.append([[2.0, 0.0, 0.0], 1.0])
        self.assertEqual(charge_distribution.calculate_oriented_electric_field(1.0, 0.0, 0.0, 1.0, 0.0, 0.0, "BOHR"),
                         0.000)
        self.assertEqual(charge_distribution.calculate_oriented_electric_field(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, "BOHR"),
                         0.000)
        self.assertEqual(charge_distribution.calculate_oriented_electric_field(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, "ANS"),
                         0.000)

    def test_oef_3_point_charges(self):
        charge_distribution = general.ChargeDistribution()
        charge_distribution.point_charge_list.append([[0.0, 0.0, 0.0], 1.0])
        charge_distribution.point_charge_list.append([[-1.0, 0.0, 0.0], 4.0])
        charge_distribution.point_charge_list.append([[-2.0, 0.0, 0.0], 9.0])
        self.assertEqual(charge_distribution.calculate_oriented_electric_field(1.0, 0.0, 0.0, 1.0, 0.0, 0.0, "BOHR"),
                         3.000)

    def test_ans_to_bohr(self):
        charge_distribution = general.ChargeDistribution()
        charge_distribution.point_charge_list.append([[1.0, 1.0, 1.0], 1.0])
        charge_distribution.ans_to_bohr()
        self.assertEqual(charge_distribution.point_charge_list,
                         [[[1.0 / 0.529177249, 1.0 / 0.529177249, 1.0 / 0.529177249], 1.0]])

    def test_bohr_to_ans(self):
        charge_distribution = general.ChargeDistribution()
        charge_distribution.point_charge_list.append([[1.0, 1.0, 1.0], 1.0])
        charge_distribution.bohr_to_ans()
        self.assertEqual(charge_distribution.point_charge_list, [[[0.529177249, 0.529177249, 0.529177249], 1.0]])

class TestQuantification(unittest.TestCase):
    def test_quantification_txt(self):
        test = titan.QuantificationTxt("chrg", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 9.0, 6.0)
        test.execute()
        efx, efy, efz, ef_tot, oef = test.quantify_selected_charge_distribution()
        self.assertAlmostEqual(oef, 0.0025000443, 6)

    def test_quantification_amber_pdb(self):
        test = titan.QuantificationPdbAmber("amber_test", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.101, 1, 152,
                                                "R(2,20)+P(35)", "PART")
        test.execute()
        efx, efy, efz, ef_tot, oef = test.quantify_selected_charge_distribution()
        self.assertAlmostEqual(oef, -0.00010160132076397886, 6)

    def test_quantification_charmm_pdb(self):
        test = titan.QuantificationPdbCharmm("charmm_test", 0.0, 0.0, 1.641, 0.0, 0.0, 0.0, 0.0, 0.0, 1.641, 4, 422,
                                                 "/", "ALL", "ANS", [350, 398], [53, 417], [365])
        test.execute()
        efx, efy, efz, ef_tot, oef = test.quantify_selected_charge_distribution()
        self.assertAlmostEqual(oef, -0.007207030321483446, 6)

    def test_quantification_log_all(self):
        test = titan.QuantificationLog("NBO", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.1010)
        test.execute()
        efx, efy, efz, ef_tot, oef = test.quantify_selected_charge_distribution()
        self.assertAlmostEqual(oef, 3.7534039842223272, 6)

    def test_quantification_log_select(self):
        test = titan.QuantificationLog("NBO", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.1010, "R(1,10)+P(12)+P(15)",
                                           "PART")
        test.execute()
        efx, efy, efz, ef_tot, oef = test.quantify_selected_charge_distribution()
        self.assertAlmostEqual(oef, 3.7904208400096633, 6)

class TestChargeDistributionCpc(unittest.TestCase):
    def test_append_point_charge(self):
        cpc_distribution = gen.ChargeDistributionCpc()
        cpc_distribution.append_point_charge(0, 0, 0, 1)
        self.assertEqual(cpc_distribution.point_charge_list, [[[0.0, 0.0, 0.0], 1.0]])

class TestCircularGenerate(unittest.TestCase):
    def test_circ_initialize_vector(self):
        cpc_calculation = titan.CircularGenerate(0.0, 0.0, 0.0, 5.0, 9.0, 6.0, 2.8, 33, 46.8279, 0.0025, "test", "ANS")
        V_X, V_Y, V_Z, unit_vector = cpc_calculation.initialize_vector()
        self.assertEqual((V_X, V_Y, V_Z, unit_vector), (5.0, 9.0, 6.0, (0.4195906791483446, 0.7552632224670202,
                                                                        0.5035088149780135)))

    def test_circ_generate_direction_vector_to_construct_plate(self):
        cpc_calculation = titan.CircularGenerate(0.0, 0.0, 0.0, 5.0, 9.0, 6.0, 2.8, 33, 46.8279, 0.0025, "test", "ANS")
        (V_X1, V_Y1, V_Z1) = cpc_calculation.generate_direction_vector_to_construct_plate()
        self.assertEqual((V_X1, V_Y1, V_Z1), (0.9077134250256691, -0.3491205480867958, -0.2327470320578639))

    def test_circ_oef_ans(self):
        cpc_calculation = titan.CircularGenerate(0.0, 0.0, 0.0, 5.0, 9.0, 6.0, 2.8, 33, 46.8279, 0.0025, "test", "ANS")
        cpc_calculation.create_and_write_plates("GAUSSIAN")
        oef = cpc_calculation.charge_distribution_cpc.calculate_oriented_electric_field(0.0, 0.0, 0.0, 5.0, 9.0, 6.0,
                                                                                      "ANS")
        self.assertAlmostEqual(oef, 0.0025)

    def test_circ_oef_bohr(self):
        cpc_calculation = titan.CircularGenerate(0.0, 0.0, 0.0, 5.0, 9.0, 6.0, 2.8, 33, 46.8279, 0.0025, "test", "BOHR")
        cpc_calculation.create_and_write_plates("GAUSSIAN")
        oef = cpc_calculation.charge_distribution_cpc.calculate_oriented_electric_field(0.0, 0.0, 0.0, 5.0, 9.0, 6.0,
                                                                                      "BOHR")
        self.assertAlmostEqual(oef, 0.0025)

class TestSpiralLineGenerate(unittest.TestCase):
    def test_sl_ef_right(self):
        sl_calculation = titan.SpiralLineGenerate("PPNNPPNPNPNPNNPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNP" +
        "NPNPNNPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNPNPNPNNPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNPNPNPN" +
        "NPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNPNPNPNNPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNPNPNPNNPPNNPN" +
        "NPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNPNPNPNNPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPN", 10, 0.1, 10.0, 0.01, 700,
                                               "RIGHT-HAND", 0.0, 0.0, 0.0, "sl_test")
        sl_calculation.create_spiral_line_distribution()
        efx, efy, efz, ef_tot = sl_calculation.charge_distribution_sl.calculate_electric_field(0.0, 0.0, 0.0, "ANS")
        self.assertAlmostEqual(efx, -0.000561, 6)
        self.assertAlmostEqual(efy, 0.003331, 6)
        self.assertAlmostEqual(efz, 0.001549, 6)

    def test_sl_ef_left(self):
        sl_calculation = titan.SpiralLineGenerate("PPNNPPNPNPNPNNPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNP" +
        "NPNPNNPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNPNPNPNNPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNPNPNPN" +
        "NPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNPNPNPNNPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNPNPNPNNPPNNPN" +
        "NPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPNPPNNPPNPNPNPNNPPNNPNNPPNNPNPNPNPNPPPPPNPNNPNPNNPNNPN", 10, 0.1, 10.0, 0.01, 700,
                                               "LEFT-HAND", 0.0, 0.0, 0.0, "sl_test")
        sl_calculation.create_spiral_line_distribution()
        efx, efy, efz, ef_tot = sl_calculation.charge_distribution_sl.calculate_electric_field(0.0, 0.0, 0.0, "ANS")
        self.assertAlmostEqual(efx, -0.000561, 6)
        self.assertAlmostEqual(efy, -0.003331, 6)
        self.assertAlmostEqual(efz, 0.001549, 6)

class TestDifferentialChargeDistribution(unittest.TestCase):
    def test_differential_distribution(self):
        charge_distribution1 = general.ChargeDistribution()
        charge_distribution1.point_charge_list.append([[0.0, 0.0, 0.0], 1.0])
        charge_distribution1.point_charge_list.append([[2.0, 0.0, 0.0], 1.0])
        charge_distribution2 = general.ChargeDistribution()
        charge_distribution2.point_charge_list.append([[0.0, 0.0, 0.0], 1.0])
        charge_distribution2.point_charge_list.append([[2.0, 0.0, 0.0], 1.0])
        differential_calculation = titan.DifferentialDistributionCalculation(charge_distribution1, charge_distribution2)
        differential_calculation.construct_differential_distribution()
        differential_calculation.differential_distribution.write_point_charge_list_to_txt_file("diff_test")
        self.assertEqual(differential_calculation.differential_distribution.calculate_oriented_electric_field(
            1.0, 0.0, 0.0, 1.0, 0.0, 0.0, "ANS"), 0.000)

class TestExamples(unittest.TestCase):
    def test_example_CPC(self):
        input_reader = input.InputReader("examples/example_CPC/TITAN_CPC.inp")
        R, N, distance, field_strength, name, out_format, point1_X, point1_Y, point1_Z, point2_X, point2_Y, point2_Z, \
        unit = input_reader.read_input_cpc()
        circular = titan.CircularGenerate(point1_X, point1_Y, point1_Z, point2_X, point2_Y, point2_Z, R, N,
                                         distance, field_strength, name, unit)
        (vector_x, vector_y, vector_z) = (point2_X - point1_X, point2_Y - point1_Y, point2_Z - point1_Z)
        circular.create_and_write_plates(out_format)
        oef = circular.charge_distribution_cpc.calculate_oriented_electric_field(point1_X, point1_Y, point1_Z, vector_x,
                                                                               vector_y, vector_z, "ANS")
        self.assertAlmostEqual(oef, 0.002500, 3)

    def test_example_CPC_alt(self):
        input_reader = input.InputReader("examples/example_CPC_alt/TITAN_CPC.inp")
        R, N, distance, field_strength, name, out_format, point1_X, point1_Y, point1_Z, point2_X, point2_Y, point2_Z, \
        unit = input_reader.read_input_cpc()
        self.assertAlmostEqual((point1_X,point1_Y,point1_Z), (0.0,1.0,2.0),1)

    def test_example_SL(self):
        input_reader = input.InputReader("examples/example_SL/TITAN_SL.inp")
        radius, N, step, chirality, name, fatom, sequence, charge, point_X, point_Y, point_Z, unit = \
            input_reader.read_input_sl()
        sl_calculation = titan.SpiralLineGenerate(sequence, fatom, charge, radius, step, N, chirality, point_X, point_Y,
                                            point_Z, name, unit)
        sl_calculation.create_spiral_line_distribution()
        efx, efy, efz, ef_tot = sl_calculation.charge_distribution_sl.calculate_electric_field(point_X, point_Y, point_Z,
                                                                                             "ANS")
        self.assertAlmostEqual(efx, -0.000561, 6)
        self.assertAlmostEqual(efy, 0.003331, 6)
        self.assertAlmostEqual(efz, 0.001549, 6)

    def test_example_SL_alt(self):
        input_reader = input.InputReader("examples/example_SL_alt/TITAN_SL.inp")
        radius, N, step, chirality, name, fatom, sequence, charge, point_X, point_Y, point_Z, unit = \
            input_reader.read_input_sl()
        self.assertAlmostEqual((point_X,point_Y,point_Z), (0.0,1.0,2.0),1)

    def test_example_quant_direction(self):
        input_reader = input.InputReader("examples/example_QUANT_DIRECTION/TITAN_QUANTIFICATION_DIRECTION.inp")
        unit, file_type, name, charge_select, charge_seq, direction, v1x, v1y, v1z, v2x, v2y, v2z, \
                    point_x, point_y, point_z = input_reader.read_input_quantification()
        force_field, n_terminal, c_terminal = input_reader.read_input_pdb()
        aspp, glup, disu = input_reader.read_input_charmm()
        name = "examples/example_QUANT_DIRECTION/" + name
        quantification_charmm = titan.QuantificationPdbCharmm(name, point_x, point_y, point_z, v1x, v1y, v1z,
                                                                  v2x, v2y, v2z, n_terminal, c_terminal, charge_seq,
                                                                  charge_select, unit, aspp, glup, disu)
        quantification_charmm.execute()
        (vector_x, vector_y, vector_z) = (v2x - v1x, v2y - v1y, v2z - v1z)
        oef = quantification_charmm.charge_distribution_to_quantify.calculate_oriented_electric_field(point_x,
                                            point_y, point_z, vector_x, vector_y, vector_z, "ANS")
        self.assertAlmostEqual(oef, -0.0211101298, 6)

    def test_example_quant_direction_alt_point(self):
        input_reader = input.InputReader("examples/example_QUANT_TXT_alt_point/TITAN_QUANTIFICATION_txt.inp")
        unit, file_type, name, charge_select, charge_seq, direction, v1x, v1y, v1z, v2x, v2y, v2z, \
                    point_x, point_y, point_z = input_reader.read_input_quantification()
        quantification_txt = quant_txt.QuantificationTxt(name, point_x, point_y, point_z, v1x, v1y, v1z, v2x, v2y, v2z,
                                                         charge_seq, charge_select, unit)
        quantification_txt.execute()
        (vector_x, vector_y, vector_z) = (v2x - v1x, v2y - v1y, v2z - v1z)
        oef = quantification_txt.charge_distribution_to_quantify.calculate_oriented_electric_field(point_x,
                                            point_y, point_z, vector_x, vector_y, vector_z, "ANS")
        self.assertAlmostEqual(oef, 0.0025025112933224816, 6)

    def test_example_quant_log(self):
        input_reader = input.InputReader("examples/example_QUANT_LOG/TITAN_QUANTIFICATION_LOG.inp")
        unit, file_type, name, charge_select, charge_seq, direction, v1x, v1y, v1z, v2x, v2y, v2z, \
                    point_x, point_y, point_z = input_reader.read_input_quantification()
        name = "examples/example_QUANT_LOG/" + name
        quantification_log = titan.QuantificationLog(name, point_x, point_y, point_z, v1x, v1y, v1z, v2x,
                                                         v2y, v2z, charge_seq, charge_select, unit)
        quantification_log.execute()
        (vector_x, vector_y, vector_z) = (v2x - v1x, v2y - v1y, v2z - v1z)
        oef = quantification_log.charge_distribution_to_quantify.calculate_oriented_electric_field(point_x,
                                            point_y, point_z, vector_x, vector_y, vector_z, "ANS")
        self.assertAlmostEqual(oef, 3.7534039842, 6)

    def test_example_quant_pdb(self):
        input_reader = input.InputReader("examples/example_QUANT_PDB/TITAN_QUANTIFICATION_PDB.inp")
        unit, file_type, name, charge_select, charge_seq, direction, v1x, v1y, v1z, v2x, v2y, v2z, \
                    point_x, point_y, point_z = input_reader.read_input_quantification()
        force_field, n_terminal, c_terminal = input_reader.read_input_pdb()
        name = "examples/example_QUANT_PDB/" + name
        quantification_amber = titan.QuantificationPdbAmber(name, point_x, point_y, point_z, v1x, v1y, v1z,
                                                                  v2x, v2y, v2z, n_terminal, c_terminal, charge_seq,
                                                                  charge_select, unit)
        quantification_amber.execute()
        (vector_x, vector_y, vector_z) = (v2x - v1x, v2y - v1y, v2z - v1z)
        oef = quantification_amber.charge_distribution_to_quantify.calculate_oriented_electric_field(point_x,
                                            point_y, point_z, vector_x, vector_y, vector_z, "ANS")
        self.assertAlmostEqual(oef, -0.0001016013, 6)

    def test_example_quant_txt(self):
        input_reader = input.InputReader("examples/example_QUANT_TXT/TITAN_QUANTIFICATION_txt.inp")
        unit, file_type, name, charge_select, charge_seq, direction, v1x, v1y, v1z, v2x, v2y, v2z, \
                    point_x, point_y, point_z = input_reader.read_input_quantification()
        quantification_txt = titan.QuantificationTxt(name, point_x, point_y, point_z, v1x, v1y, v1z,
                                                                  v2x, v2y, v2z, charge_seq, charge_select, unit)
        quantification_txt.execute()
        (vector_x, vector_y, vector_z) = (v2x - v1x, v2y - v1y, v2z - v1z)
        oef = quantification_txt.charge_distribution_to_quantify.calculate_oriented_electric_field(point_x,
                                            point_y, point_z, vector_x, vector_y, vector_z, "ANS")
        self.assertAlmostEqual(oef, 0.0025000443, 6)

if __name__ == '__main__':
    unittest.main()
