% include('head.tpl')
		<!-- Banner -->
			<section id="banner">
				<h2>LoL  Straw</h2>
				<h4><a href="/">Personajes	</a></h4><h4><a href="/objetos">Objetos</a></h4>
			</section>

		<!-- Table -->
			</section>
			<section class="box">
				<h3>Objetos</h3>
				<div class="table-wrapper">
					<table>
					

%for key, value in datos.iteritems():
						<tr>
							<td>{{value[0]}} </td>
							<td>{{!value[1]}} </td>
						</tr>
%end
					</table>

				</div>
			</section>
% include('foot.tpl')

