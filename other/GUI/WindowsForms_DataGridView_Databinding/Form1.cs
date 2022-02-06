using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp4
{
    public partial class Form1 : Form
    {
        List<DgvRow> dgvDataSource;

        public Form1()
        {
            InitializeComponent();

            dgvDataSource = new List<DgvRow>();
            UpdateDgvView();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < 10; i++)
            {

                DgvRow row = new DgvRow()
                {
                    No = dgv.Rows.Count + 1 + i,
                    Name = "Hihi" + (dgv.Rows.Count + 1 + i).ToString(),
                    Class = "Class" + (dgv.Rows.Count + 1 + i).ToString()
                };

                dgvDataSource.Add(row);
            }

            UpdateDgvView();
        }

        private void UpdateDgvView()
        {
            if (dgvDataSource.Count == 0 && dgv.DataSource == null) return;

            dgv.DataBindingComplete -= dataGridView1_DataBindingComplete;
            dgv.DataBindingComplete += dataGridView1_DataBindingComplete;
            
            dgv.DataSource = null;
            dgv.DataSource = dgvDataSource;
            //dgv.Update();
            //dgv.Refresh();
        }

        private void dataGridView1_DataBindingComplete(object sender, DataGridViewBindingCompleteEventArgs e)
        {
            if (dgv.Columns.Count > 0)
            {
                dgv.Columns[0].ReadOnly = true;

            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            dgvDataSource.Clear();
            UpdateDgvView();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            foreach (var row in dgvDataSource)
            {
                Console.WriteLine($"{row.No} - {row.Name} - {row.Class}");
            }
            Console.WriteLine(@"\n\n\n\");
        }

        private void btnInsert_Click(object sender, EventArgs e)
        {
            DgvRow row = new DgvRow()
            {
                No = dgv.Rows.Count + 1
            };

            dgvDataSource.Add(row);
            UpdateDgvView();
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            Console.WriteLine($"Selected number :");

            if (dgv.SelectedRows.Count == 0) return;

            List<int> deleteListIndex = new List<int>();
            for (int i = 0; i < dgv.SelectedRows.Count; i++)
            {
                deleteListIndex.Add(dgv.SelectedRows[i].Index);
            }

            deleteListIndex.Sort();
            for (int i = deleteListIndex.Count - 1; i >= 0; i--)
            {
                Console.WriteLine(deleteListIndex.ElementAt(i));
                dgvDataSource.RemoveAt(deleteListIndex.ElementAt(i));
            }
            UpdateDgvView();
        }
    }

    public class DgvRow
    {
        public int No { set; get; } = 0;
        public string Name { set; get; }
        public string Class { set; get; }
    }
}
